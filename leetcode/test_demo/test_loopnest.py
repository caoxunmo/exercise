# -*- encoding:utf-8 -*-

#循环嵌套：
"""
循环嵌套就是把内层循环当作外层循坏的循环体，只有内层循环为假（0）时，
才能跳出内层循环，从而结束外层循环的当次循环；内（m）,外（n）,得总循
环次数为（m*n）
"""
def loopnest():
    for i in range(5):
        j = 0
        while j <= 3:
            print ("i的值：%s；j的值：%s" % (i,j))
            break
        print("内循环结束")
#            j += 1
#loopnest()

#break的用法：
def break_usage():
    for i in range(0, 10):
        print("i的值是: %s" % i)
        if i == 4:
            # 执行该语句时将结束循环
            break
#break_usage()


#continue的用法：
#筛选出奇数
def continue_usage():
    for i in range(10):
        if i % 2 == 0:
            continue
        print("奇数有：%s" % i)
continue_usage()