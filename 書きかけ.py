import binascii
import string

def crc_srec(hexstr):
    crc = sum(bytearray(binascii.unhexlify(hexstr)))
    crc &= 0xff
    crc ^= 0xff
    return crc

def address_conv_srec(record):
    size = int(record[2:4], 16)
    type_ = record[1:2]
    address_top2 = record[4:6]
    line = record[2:-2]
    return 'S{}{}{:02X}'.format(type_, line, crc_srec(line))
