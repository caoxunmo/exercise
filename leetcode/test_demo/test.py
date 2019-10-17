# -*- encoding:utf-8 -*-

# for i in range(5):
#     for j in range(3):
#         print(i, j)

'''
a = [1, 2, 3, "数字"]

x = id(a)
y = id(a[:])
lenth = len(a)

print(a)
print(x, y)
print(lenth)



#print和return的区别：
def test1(target):
    str = target
    print("this is %s" % str)

def test2(target):
    str = target
#    return "this is %s" % str
    print "this is %s" % str

test1("print")
test2("return")
'''

#tuple元组详解：

#当创建的元组只有一个元素时，元组后面必加一个逗号
tuple_demo1 = ("中文",)
print(type(tuple_demo1))
#不加逗号，将其误认为字符串
tuple_demo2 = ("中文")
print(type(tuple_demo2))