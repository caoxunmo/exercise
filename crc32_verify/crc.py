# -*- encoding:utf-8 -*-

import binascii
def ComputeFileCRC(filename):
    try:
        blocksize = 1024 * 64
        f = open(filename, "rb")
        str = f.read(blocksize)
        crc = 0
        while len(str) != 0:
            crc = binascii.crc32(str, crc) & 0xffffffff
            str = f.read(blocksize)
        f.close()
    except:
        print "compute file crc failed!"
        return 0
    return crc

print (ComputeFileCRC(fool.text))

