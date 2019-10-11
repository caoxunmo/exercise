# -*- encoding:utf-8 -*-

'''
def sum_even(n):
    sum = 0
    for i in range(n):
        if i % 2 == 0:
            sum += i
    return sum
12
print (sum_even(10))



#求0-n中1的个数：
num = int(input("查询的数字：\n"))
count = 0

for i in range(num+1):
    num_1 = str(i).count('1')
    count +=num_1
print (count)
'''


#得到一个list当中所有元素的和以及乘积

sum = 0
mul = 1
target_list = [1, 2, 3, 4, 5]

for item in target_list:
    sum += item
    mul *= item

print("和是：%s" % sum)
print("乘积是：%s" % mul)

