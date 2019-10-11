# -*- encoding:utf-8 -*-

para_input = int(raw_input("输入n的值："))
print (type(para_input))
count = 0

for i in range(para_input+1):
    num = str(i).count("1")
    count += num
print (count)