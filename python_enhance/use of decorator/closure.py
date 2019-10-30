# -*- encoding:utf-8 -*-

#闭包：内部函数可以访问外部函数的参数
def outer(a, b):
    print(a+2, b+2)
    def inner():
        print(a+1, b+1)
    return inner


#result = outer(11, 22)
#print(result)
#result()

'''
装饰器是闭包得的实现，闭包一般传变量进去；装饰器是传
函数名进去。@会把下面被装饰的函数作为一个参数传递给
装饰器，然后把装饰器的返回值赋值给被装饰的函数名,最终
被装饰的函数名保存的是装饰器的内部函数的地址。
'''
#简单装饰器的应用：
def buy_way(func):
    print("开始执行")
    def wrapper():
#        print(func.__name__)
        print("线上购买")
        func()
    return wrapper()

@buy_way
def cooking():
    print("洗菜")
    print("炒菜")
    print("上菜")



'''
#装饰器的参数传递：
def buy_online(param):
    def platform(func):
        def wrapper():
            print("%s线上购买" % param)
            func()
        return wrapper()

@buy_online('每日优鲜')
def making(*args, **kwargs):
    print("洗菜")
    print("炒菜")
    print("上菜")
'''