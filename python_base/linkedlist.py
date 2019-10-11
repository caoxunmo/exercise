# -*- encoding:utf-8 -*-

import copy

'''
链表：是一种物理存储单元上非连续、非顺序的存储结构，数据元素的逻辑顺序是通过链表中的指针链接次序实现的
分为：单向链表：它的每个节点包含两个域，信息域（data）、链接域（next），这个链接指向链表中的下一个节点，
        而最后一个节点的链接域则指向一个空值；
      双向链表：除了包含单链表的部分,还增加的pre前一个节点的指针。
'''

# 单链表
class Node():
    """
    节点类
    """
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class SingleLinkList():

#单链表
    def __init__(self, node=None):
        self.__head = node              #私有变量

#判断是否为空
    def is_empty(self):
        return self.__head == None


'''
对象赋值实际上是对象引用（内存地址）传递，由于will和wilber
指向同一个对象，所以对will的任何修改都会体现在wilber上;
两地址是一样;
y会随着x里的某元素改变而改变，由于内存地址相同
'''

x = ["first", "second", 88, ["third", "fourth", 89]]
y = x

"""
print (id(x))
print (id(y))
print [id(i) for i in x]
print [id(i) for i in y]
"""

#x[0] = "dif"
#print x
#print y

"""
浅拷贝：
浅拷贝会拷贝父对象，不会拷贝子对象
"""


z = copy.copy(x)
#print z
print (id(x))
print (id(z))
print [id(i) for i in x]
print [id(i) for i in z]

