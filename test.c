#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/ioctl.h>
#include <fcntl.h>
#include <termios.h>
#include <unistd.h>
#include <stdbool.h>
#include <string.h>

#define SOH 0x01
#define STX 0x02
#define EOT 0x04
#define ACK 0x06
#define NAK 0x15
#define CAN 0x18
#define SUB 0x1a

static unsigned char g_buf[64 * 1024 * 1024];

static int OpenSerialRaw(char *devport, int speed, bool isBlock){
	int fd;
	struct termios tio;
	memset(&tio, 0, sizeof(tio));
	if(isBlock){
		fd = open(devport, O_RDWR);
	}else{
		fd = open(devport, O_RDWR | O_NONBLOCK);
	}
	if(fd < 0){		
		return fd;	/* error */
	}
	tio.c_cflag |= CREAD;
	tio.c_cflag |= CLOCAL;
	tio.c_cflag |= CS8;
	cfsetispeed(&tio, speed);
	cfsetospeed(&tio, speed);
	cfmakeraw(&tio);
	tcsetattr(fd, TCSANOW, &tio);
	ioctl(fd, TCSETS, &tio);
	return fd;
}

unsigned short updcrc(unsigned char c, unsigned short crc){
	int i;
	crc ^= (((unsigned short)c) << 8);
	for(i = 0; i < 8; i++) {
		if (crc & 0x8000) {
			crc = (crc << 1) ^ 0x1021;
		} else {
			crc <<= 1;
		}
	}
	return crc;
}

static int recv_bytes(int fd, unsigned char *buf, int size){
	int i = 0, ret;
	while(i < size){
		ret = read(fd, &buf[i], 1);
		if(1 == ret){
			i++;
		}else if(0 > ret){
			return -1;
		}
	}
	return size;
}

static int recv_bytes_crc(int fd, unsigned char *buf, int size, unsigned short *pcrc){
	int i = 0, ret;
	*pcrc = 0;
	while(i < size){
		ret = read(fd, &buf[i], 1);
		if(1 == ret){
			*pcrc = updcrc(buf[i], *pcrc);
			i++;
		}else if(0 > ret){
			return -1;
		}
	}
	return size;
}

static int recv_start_byte(int fd){
	char buf;
	int len = recv_bytes(fd, &buf, 1);
	if(len == 1){
		if(buf == SOH){
			return 128;
		}else if(buf == STX){
			return 1024;
		}else if(buf == EOT){
			return -1;
		}else if(buf == CAN){
			/* キャンセルもエラーとする */
			return 0;
		}
	}
	return 0;
}

static unsigned short swap16(unsigned short value)
{
    unsigned short ret;
    ret  = value << 8;
    ret |= value >> 8;
    return ret;
}

static int xmodem_recv(int fd, unsigned char *buf){
	int ret = 0, i, block_len, len;
	unsigned char c = 'C', blockno[2];
	unsigned short rcv_cksum, calc_cksum;
	/* スタート送信 */
	write(fd, &c, 1);
	while(true){
		/* ブロックスタート,転送終了,キャンセル等受信 */
		block_len = recv_start_byte(fd);
		if(block_len == 0){
			return 0;
		}else if(block_len == -1){
			/* 転送終了 */
			c = ACK;
			write(fd, &c, 1);
			break;
		}
		/* ブロックNo受信 */
		len = recv_bytes(fd, blockno, 2);
		if(len != 2){
			return 0;
		}
		//printf("block[0x%02x,0x%02x] start size=%dbyte\n", blockno[0], blockno[1], block_len);
		/* ブロック受信 */
		len = recv_bytes_crc(fd, buf, block_len, &calc_cksum);
		if(len != block_len){
			printf("err[1] len=%d\n", len);
			for(i = 0; i < len; i++){
				printf("buf[%d]=0x%02x\n", i, buf[i]);
			}
			return 0;
		}
		/* チェックサム受信 */
		len = recv_bytes(fd, (unsigned char *)&rcv_cksum, 2);
		if(len != 2){
			printf("err[2] len=%d\n", len);
			return 0;
		}
		rcv_cksum = swap16(rcv_cksum);
		printf("block[%d] recv_cksum=0x%x, calc_cksum=0x%x\n", blockno[0], rcv_cksum, calc_cksum);
		/* ACK返信 */
		c = ACK;
		write(fd, &c, 1);
		ret += block_len;
		buf += block_len;
	}
	return ret;
}

int main(void){
	int fd, size;
	printf("Start\n");
	fd = OpenSerialRaw("/dev/serial0", B921600, true);
	size = xmodem_recv(fd, g_buf);
	close(fd);
	if(size > 0){
		FILE *fp = fopen("recv.bin", "wb");
		if(fp){
			fwrite(g_buf, size, 1, fp);
			fclose(fp);
		}
	}
	printf("End\n");
	return 0;
}
