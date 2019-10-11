# -*- encoding:utf-8 -*-

i = input("输入a值：")
j = input("输入b值：")

try:
    n = i / j
except ZeroDivisionError as a:
    print("except:", a)
else:
    print ("结果：%s" % n)


'''
i = 0
j = 12
try:
    n = j / i
except ZeroDivisionError as e:
    print("except:",e)

'''

