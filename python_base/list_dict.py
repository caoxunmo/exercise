# -*- encoding:utf-8 -*-

#定义一个判断列表里是否存在该元素的方法
def add_ele(a, b=0):
    list1 = []
    while a not in list1:
        b += 1
        list1.append(b)
        print list1

# add_ele(10)