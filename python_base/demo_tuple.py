# -*- encoding:utf-8 -*-

#tuple元组详解：

#当创建的元组只有一个元素时，元组后面必加一个逗号
tuple_demo1 = ("中文",)
print(type(tuple_demo1))
#不加逗号，将其误认为字符串
tuple_demo2 = ("中文")
print(type(tuple_demo2))

