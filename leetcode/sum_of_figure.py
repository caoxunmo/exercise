# -*- encoding:utf-8 -*-

import time

"""
两数之和：
给定一个整数数列，找出其中和为特定值的那两个数，你可以
假设每个输入都只会有一种答案，同样的元素不能被重用。
"""

#nums = [11, 15, 2, 7]
#target = 9

nums = [5, 4, 7, 5, 7]
target = 10

def twoSum1():
    lens = len(nums)
    for i in range(lens):
        for j in range(i+1, lens):
            if nums[j] == target - nums[i]:
                print (nums[i], nums[j])
            else:
                continue

def twoSum2():
    lens = len(nums)
    for i in range(lens):
        y = target - nums[i]
        if y in nums:
            j = nums.index(y)
            if j != i:
                if j < i:
                    print (j, i)

def twoSum3():
    lens = len(nums)
    d = {}
    for x in range(lens):
        a = target - nums[x]
        if nums[x] in d:
            print d[nums[x]], x
        else:
            d[a] = x

#def twoSum4():
hashmap = {}
for ind, num in enumerate(nums):
#    print ("1:%s" % ind)
#    print ("2:%s" % num)

    hashmap[num] = ind             #放入字典中
#    print ("values：%s" % hashmap.values())
#    print ("keys：%s" % hashmap.keys())

for i, num in enumerate(nums):
    j = hashmap.get(target - num)
    if j is not None and i != j:
        print [i, j]



'''
start = time.clock()
twoSum3()
end = time.clock()
print ("程序运行的时间：%s" % (end - start))
'''