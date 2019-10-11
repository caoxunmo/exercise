# -*- encoding:utf-8 -*-

#None、空列表[]、空字典{}、空元组()、0等一系列代表空和无的对象会被转换成False；其他有意义的都为True
element = [None, False, "", 0, [], {}, (), "target"]

#if 对逻辑表达式进行判断；if not 是逻辑非判断
for i in element:
    if not i:
        print ("反向")
    else:
        print ("正向")

for i in element:
    if i:
        print ("反向")
    else:
        print ("正向")

for j in element:
    print (not j)