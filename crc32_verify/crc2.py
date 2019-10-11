# -*- encoding:utf-8 -*-

#crc32循环冗余效验

from zlib import crc32

def getCrc32(filename):
    with open(filename, 'rb') as f:
        return crc32(f.read()) & 0xffffffff

print('{:8} {:x}'.format('crc32:', getCrc32('fool.text')))
#print type(getCrc32('fool.text'))
