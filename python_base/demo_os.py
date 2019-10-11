# -*- encoding:utf-8 -*-

import os

#r表示字符串内按原始含义解释，不做转义处理
paper = open(r"D:\python_workspace\exercise\crc32_verify\test.text", "w+")             #文件绝对路径,前面带上r

#os.linesep代表当前系统上的换行符
paper.write("这是一个python文件1"+os.linesep)                                          #单个字符串

paper.writelines(("这是一个python文件2"+os.linesep, "this is two"+os.linesep))        #多个字符串

#print (paper.tell())

paper.seek(os.SEEK_SET)                                 #设置指针回到文件最初

print(paper.tell())
print(paper.read())
paper.close()


#查看文件关闭状态
#print(paper.closed)

print ("新建的文件名：%s" % paper.name)



