# -*- encoding:utf-8 -*-

import binascii

'''
binascii模块包含很多在二进制和ASCII编码的二进制表示转换的方法。
通常情况不会直接使用这些功能，而是使用像UU，base64编码，或BinHex封装模块。
binascii模块包含更高级别的模块使用的，用C语言编写的低级高效功能。
'''

#python内置函数

a = hex(88)                     #把十进制转换为十六进制
print (a)

b = 1.23.hex()
print (b)                       #把浮点型转换成16进制

'''
内置函数hex和binascii.hexlify()的区别就
在于hex只能接受整形不能接受字符串
'''
try:
    c = hex('88')
except TypeError as i:
    print ("错误原因：%s" % i)

#把十进制转换为二进制字符
print ("88的二进制结果：%s" % bin(88))
print ("8的二进制结果：%s" % bin(8))

#把十进制转化为八进制字符
print ("88的八进制结果：%s" % oct(88))
print ("500的八进制结果：%s" % oct(500))

#把一个整形转换成ASCII码表中对应的单个字符
print (chr(98))
print (chr(99))

#把ASCII码表中的字符转换成对应的整形
print (ord('a'))
print (ord('b'))

#binascii里的参数用法
s = 'abcde'
d = binascii.b2a_hex(s)                 #把字符串转换为16进制的
d_same = binascii.hexlify(s)

e = binascii.a2b_hex(d)                 #把16进制的转换为字符串
e_same = binascii.unhexlify(d_same)
print (d, e)
print (d_same, e_same)


