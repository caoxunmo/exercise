# -*- encoding:utf-8 -*-

import logging

'''不带参数的装饰器用法：'''

def use_logging(func):
    def wrapper():
        logging.warn("%s is running" % func.__name__)       #fun.__name__：表示程序当前运行在哪一模块中
        return func()
    return wrapper

#@是装饰器的语法糖，省去了赋值的操作；@相当于result=use_logging(foo)。
#@use_logging
def foo():
    print("i am foo")

#foo()
#result = use_logging(foo)       #装饰器use_logging(foo)返回时函数对象是wrapper
#result()                        #相当于执行wrapper（）


"""带参数修饰器的用法："""

def outer(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == "warn":
                logging.warn("%s is running" % func.__name__)
            elif level == "info":
                logging.warn("%s is running" % func.__name__)
            return func(*args)
        return wrapper
    return decorator

@outer(level='warn')
def event(name=None):
    print("I am %s" % name)

event("jcak")



'''
装饰器总结：
def myDecorator(param):                                 #定义装饰器，可能带参数
    def decorator(func):                                #装饰器核心，已被装饰的函数对象为参数，返回装饰后的函数对象
        def wrapper(*args, **kwargs):                   #装饰过程，参数列表适应不同参数的函数
            ....                        #修改函数调用前的行为
            func(*args, **kwargs)       #调用函数
            ....                        #修改函数调用后的行为
        return wrapper                  
    return decorator

@myDecorator(param="param")                     #给函数加上装饰器
def myfunc(param):
    ...
'''