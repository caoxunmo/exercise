# -*- encoding:utf-8 -*-

import os
import time

#对脚本进一步完善，不希望出现特殊字符等
#代码运行时间太长，需要优化

host = raw_input("输入IP：")

a = time.clock()
forbidden = ["$", ",", "/", "*"]
for i in forbidden:
    if i in host:
        print ("非法字符")
    else:
        result = os.popen("ping %s" % host).read()

if "TTL" in result:
    print ("IP：%s是通的" % host)
else:
    print ("IP不通")
b = time.clock()
print (b-a)

