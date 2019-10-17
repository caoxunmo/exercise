# -*- encoding:utf-8 -*-

import json

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


#解决列表无法正常输出中文：
list_word = ["动物", "植物", "人", "环境"]
print("无法正常显示：%s" % list_word)

#1.
mean1 = str(list_word).decode('string_escape')
print("方法1：%s" % mean1)

#2.通过改成json格式
mean2 = json.dumps(list_word, encoding='UTF-8', ensure_ascii=False)
print(mean2)
