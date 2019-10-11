# -*- encoding:utf-8 -*-

import pymysql


#创建数据库连接

con = pymysql.connect(host='192.168.50.130',
                      port=3306,
                      user='root',
                      password='Caoxun1!',
                      db='test',
                      charset='utf8'
)
#使用cursor()方法创建一个游标对象cursor
cursor = con.cursor()

#cursor.execute("drop table if exists employee")

sql = '''create tabel employee(
            id int not null,
            name char(20),
            age int(5),
            sex char(2),
            salary float)   
'''

try:
    cursor.execute(sql)
except Exception as e:
    con.rollback()
    print (e)


effect_row = cursor.execute("show tables")
print (effect_row)
print (cursor.fetchone())
con.commit()




