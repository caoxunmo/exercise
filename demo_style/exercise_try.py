# -*- encoding:utf-8 -*-

from selenium import webdriver


if "1" != 1:
    print ("equal")
else:
    print ("same")



'''
raise后不接异常类参数时，默认RuntimeError
raise后接的异常类参数必须属于BaseException
'''
try:
    if '1' != 1:
        raise ValueError
    else:
        print ("no Error")
except ValueError:
    print ("Error occured")

    
    

