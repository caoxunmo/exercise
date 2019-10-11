# -*- encoding:utf-8 -*-

import pymysql


class LinkSql():
    def __init__(self, host, port, user, passwd, db):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.db = db

    def connect(self):
        self.database = pymysql.connect(self.host, self.port, self.user, self.passwd, self.db)
        self.cursor = self.database.cursor()

    def close(self):
        self.cursor.close()
        self.database.close()