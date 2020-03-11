import sys

crctab = [0]*256

UNSIGNED = lambda n: n & 0xffffffff

def crc32(data):
    crc = 0xffffffff
    for c in data:
        crc = crc ^ c
        for i in range(8):
            crc = (crc >> 1) ^ (0xedb88320 * (crc & 1))
    return 0xffffffff ^ crc

def mkcksumtbl():
    for i in range(256):
        c = UNSIGNED((i << 24))
        for j in range(8, 0, -1):
            if (c & 0x80000000) != 0:
                c = UNSIGNED((c << 1)) ^ 0x04c11db7
            else:
                c = UNSIGNED((c << 1))
        crctab[i] = c

def cksum(data):
    crc = 0
    for c in data:
        crc = UNSIGNED((crc << 8)) ^ crctab[(crc >> 24) ^ c]
    n = len(data)
    while n:
        c = n & 0o0377
        n = n >> 8
        crc = UNSIGNED((crc << 8)) ^ crctab[(crc >> 24) ^ c]
    return UNSIGNED(~crc)
        
if __name__ == '__main__':
    fname = sys.argv[-1]
    buffer = open(fname, 'rb').read()
    mkcksumtbl()
    print("%d %d %s" %  (cksum(buffer), len(buffer), fname))
    print("%d %d %s" %  (crc32(buffer), len(buffer), fname))
