import sys

crctab = [0]*256
crctab_pol = [0]*256

UNSIGNED = lambda n: n & 0xffffffff

def mkcrctbl():
    for i in range(256):
        c = i
        for j in range(8):
            if (c & 1) != 0:
                c = 0xedb88320 ^ (c >> 1)
            else:
                c = (c >> 1)
        crctab[i] = c

def mkcrctbl_pol():
    for i in range(256):
        c = UNSIGNED((i << 24))
        for j in range(8):
            if (c & 0x80000000) != 0:
                c = UNSIGNED((c << 1)) ^ 0x04c11db7
            else:
                c = UNSIGNED((c << 1))
        crctab_pol[i] = c

def crc32(data):
    crc = 0xffffffff
    for c in data:
        crc = crctab[(crc ^ c) & 0xff] ^ (crc >> 8)
    return crc ^ 0xffffffff

def crc32_pol(data):
    crc = 0
    for c in data:
        crc = UNSIGNED((crc << 8)) ^ crctab_pol[(crc >> 24) ^ c]
    return crc


def cksum(data):
    crc = crc32_pol(data)
    n = len(data)
    while n:
        c = n & 0o0377
        n = n >> 8
        crc = UNSIGNED((crc << 8)) ^ crctab_pol[(crc >> 24) ^ c]
    return UNSIGNED(~crc)
        
if __name__ == '__main__':
    fname = sys.argv[-1]
    buffer = open(fname, 'rb').read()
    mkcrctbl()
    mkcrctbl_pol()
    print("%d %d %s" %  (cksum(buffer), len(buffer), fname))
    print("%d %d %s" %  (crc32(buffer), len(buffer), fname))
