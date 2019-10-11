# -*- encoding:utf-8 -*-


#变量转换的demo
'''
a = raw_input("请输入：")
b = int(a)

print("a的类型：%s" % type(a))
print("b的类型：%s" % type(b))
print (b)
'''


#从一个给定文件中读入一个长度不超过100的字符串，删除其中的重复字符
result_list = []
with open("target_file.txt") as f:
    chars_list = f.read()
    for c in chars_list:
        if c not in result_list:
            result_list.append(c)
print (result_list)
