# -*- encoding:utf-8 -*-

import os

#实现检测网络是否ping得通

host = raw_input("输入IP：")
#print (type(host))
result = os.popen("ping %s" % host).read()
#print ("DEBUG：%s" % result)

if "TTL" in result:
    print ("IP：%s是通的" % host)
else:
    print ("IP不通")





