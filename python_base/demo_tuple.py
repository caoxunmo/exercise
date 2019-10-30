# -*- encoding:utf-8 -*-

"""
tuple元组详解：
    元组不仅用做不可变的列表，还可以用于没有字段名的记录。
    元组其实是对数据的记录：
        元组中的每个元素都存放了记录中一个字段的数据，外加这个字段的位置；
        正是这个位置信息给数据赋予了意义。
"""

#当创建的元组只有一个元素时，元组后面必加一个逗号
tuple_demo1 = ("中文",)
print(type(tuple_demo1))
#不加逗号，将其误认为字符串
tuple_demo2 = ("中文")
print(type(tuple_demo2))

#元组拆包：
coordinate = (33, -118)
#print(type(coordinate))
latitute, longitute = coordinate
print(longitute)

#将元组的元素分别赋值给变量：
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)

#不使用中间变量交换两变量的值：
a, b = 1, 2
b, a = a, b
print(a, b)
