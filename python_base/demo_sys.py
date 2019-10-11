# -*- encoding:utf-8 -*-

import os,sys


#生成新的文件路劲
curr_path = os.path.realpath(__file__)
curr_dir = os.path.dirname(curr_path)
case_path = os.path.join(curr_dir, "report.html")

print(case_path)





"""
#获取当前文件的路径
# __file__表示当前文件的path
curr_path = os.path.realpath(__file__)
print("当前文件路径：%s" % curr_path)

#当前文件的上一级目录
curr_path_dir = os.path.dirname(curr_path)
print("当前文件的目录：%s" % curr_path_dir)

#获取文件名
file_name = os.path.basename(curr_path)
print("文件名：%s" % file_name)
"""









'''
path = sys.path
base_path = os.getcwd()

print(path)
print(sys.path[0])
#print(base_path)
add_path = sys.path.append(base_path)
if base_path == sys.path[0]:
    print("same")
    print(base_path, sys.path[0])
else:
    print("equal")
'''