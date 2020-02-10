#!/usr/bin/python3
import sys
import binascii

args = sys.argv
file_name = args[1]
with open(file_name, 'rb') as ifile:
    rdata = ifile.read()
    print("0x%8x" % binascii.crc32(rdata))

