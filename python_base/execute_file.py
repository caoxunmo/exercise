# -*- encoding:utf-8 -*-

import os

'''
# 打开一个文件
fo = open(r"D:\python_workspace\exercise\crc32_verify\fool.text", "r+")

# 读取文件里的字符串
string = fo.read()
print ("文件内容：%s" % string)

# 判断文件指针的位置
site = fo.tell()
print ("指针当前位置：%s" % site)

# 移动指针读取文件里指定内容
fo.seek(2, 0)                                                       #从头开始，指针移到移动到第2处
new_site = fo.tell()
string = fo.read()
print ("新定的位置：%s,所读的文件内容：%s" % (new_site,string))

# 读取一个字节,指针自动后移一个位置
fo.seek(3, 0)
print("开始的位置：%s" % fo.tell())
fo.read(1)
print("之后的位置：%s" % fo.tell())


# 关闭打开的文件
# fo.close()
print ("文件状态：%s" % fo.closed)
'''


'''
with的用法
with.....as语句是简化版的try except finally语句
会自动关闭文件，处理上下文环境的异常
'''
with open("with.text", "r") as f:
    for row in f:
        print(row)
#   print (f.read())

#with的工作原理
class Sample:
    def __init__(self):
        pass

    def __enter__(self):
        print('__enter__')
        return "foo"

    def __exit__(self, exc_type, exc_val, exc_tb):
        print ('__exit__')
        return True

def get_instance():
    return Sample()

with get_instance() as demo:
    print ("demo:%s" % demo)


# fo.write("this is good\n good time\n")

# print ("文件名：%s" % fo.name)
# print ("文件的关闭状态：%s" % fo.closed)
# print ("访问模式：%s" % fo.mode)
# print ("末尾是否强制加空格 :%s" % fo.softspace)



