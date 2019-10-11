# -*- encoding:utf-8 -*-

'''
在__init__中定义self.__*(name),其中self.__*是类变量名,name、level
是传入Teacher类的参数名，这里的__init__作用是定义了类变量名，
将外部的所有参数传给类变量名里。
'''


class Teacher():
    def __init__(self, name=None, level=None):
        self.__name = name
        self.__level = level

#定义一个获取私有变量的方法：
    def get_name(self):
        return self.__name

    def get_level(self):
        return self.__level

#定义一个修改私有变量的方法：
    def modify_name(self, name):
        self.__name = name
        return self.__name


teacher = Teacher("cx", 7)
level = teacher.get_level()
print (level)

before_name = teacher.get_name()
after_name = teacher.modify_name("jmz")

print ("私有变量修改之前：%s，修改之后：%s" % (before_name,after_name))

