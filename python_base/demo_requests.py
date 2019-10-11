# -*- encoding:utf-8 -*-

import requests

def getData(url):
    data = requests.get(url)
    print data.content
#    return data.content








