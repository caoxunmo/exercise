# -*- encoding:utf-8 -*-

import json

dict = {}
dict["1"] = {"name": "xiaohua"}
dict["2"] = {"sex": "boy"}
dict["3"] = {"age": "twenty"}
#print(dict)

#使用json格式存储数据：
def store_data():
    with open('with.text', 'r+') as f:
        json.dump(dict, f)


#从json文件中读取数据（open默认r权限）：
def read_data():
    with open('with.text', 'r')as file:
        json.load(file)
    #    print(dict['1']['name'])
        for i in dict:
            print(i, dict[i])

#将json类型转换为python类型，并读出想要的数据：
def get_data(route):
    with open(route) as f:
        pop_data = json.load(f)
#        print(pop_data)
#        print("DEBUG：%s" % type(pop_data))
        for pop_dict in pop_data:
            year = pop_dict['Year']
            if year == '2000':
                name = pop_dict['Country Name']
                code = pop_dict['Country Code']
                value = pop_dict['Value']
#                result = name + code + value
#                print(result)
                print("%s:%s:%s" % (name, code, value))
#                return "%s:%s:%s" % (name, code, value)


path = 'D:\json\population_data.json'
data = get_data(path)












