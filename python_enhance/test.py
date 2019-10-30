# -*- encoding:utf-8 -*-

'''
def kw_dict(**kwargs):
    print kwargs

kw_dict(a=1, b=2, c=33)
'''

def w1(fun):
    print('...装饰器开始装饰...')
    def inner():
        print('...验证权限...')
        fun()
    return inner

@w1
def test():
    print('test')

#test()


def demo(a, b):
    return a+b

result = demo       #相当于把函数放入变量里
#print(result(1, 2))


def hi(name):
    def greet():
        return "now you are in the greet() function"
    def welcome():
        return "now you are in the welcome() function"

    if name == 1:
        return greet
    else:
        return welcome

a = hi(1)
print(a)            # 'a'指向于hi()函数里中的greet()函数
print(a())          # 同理于print(hi(1)())

def sum(a, b):
    c = a + b
    return c
