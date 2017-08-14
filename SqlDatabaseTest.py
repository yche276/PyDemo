
"""
# import mysql.connector as mysqldb
import MySQLdb as mysqldb

import sys


reload(sys)
sys.setdefaultencoding('utf-8')

__db_username = 'webcrawler'
__db_password = 'Monday123'
__db_host = '192.168.1.75'

__db_name_realestatecom = 'realestate'
__db_realestate_table_districts = 'tb_districts'
__db_realestate_table_regions = 'tb_regions'
__db_realestate_table_suburbs = 'tb_suburbs'

# con = mysqldb.connect(user=__db_username,
#                           password=__db_password,
#                           host=__db_host,
#                           database=__db_name_realestatecom)



con = mysqldb.connect(host=__db_host,
                      user=__db_username,
                      passwd=__db_password,
                      db=__db_name_realestatecom)
cursor = con.cursor()
query = "SELECT * FROM {}".format(__db_realestate_table_regions)
ret_regions = []
try:
    cursor.execute(query)
    for (region_id, region_name) in cursor:
        region = (region_id, region_name)
        ret_regions.append(region)
except mysqldb.Error, e:
    print e
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()

print ret_regions
"""

#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
from multiprocessing import Pool
import mysql.connector.pooling

__db_name_realestatecom = 'realestate'
__db_realestate_table_districts = 'tb_districts'
__db_realestate_table_regions = 'tb_regions'
__db_realestate_table_suburbs = 'tb_suburbs'


dbconfig = {
    "host":"127.0.0.1",
    "port":"3306",
    "user":"root",
    "password":"a6t7c8c7",
    "database":"realestate",
}


class MySQLPool(object):
    """
    create a pool when connect mysql, which will decrease the time spent in
    request connection, create connection and close connection.
    """
    def __init__(self, host="172.0.0.1", port="3306", user="root",
                 password="123456", database="test", pool_name="mypool",
                 pool_size=3):
        print "init"
        res = {}
        self._host = host
        self._port = port
        self._user = user
        self._password = password
        self._database = database

        res["host"] = self._host
        res["port"] = self._port
        res["user"] = self._user
        res["password"] = self._password
        res["database"] = self._database
        self.dbconfig = res
        self.pool = self.create_pool(pool_name=pool_name, pool_size=pool_size)

    def create_pool(self, pool_name="mypool", pool_size=3):
        """
        Create a connection pool, after created, the request of connecting
        MySQL could get a connection from this pool instead of request to
        create a connection.
        :param pool_name: the name of pool, default is "mypool"
        :param pool_size: the size of pool, default is 3
        :return: connection pool
        """
        pool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name=pool_name,
            pool_size=pool_size,
            pool_reset_session=True,
            **self.dbconfig)
        return pool

    def close(self, conn, cursor):
        """
        A method used to close connection of mysql.
        :param conn:
        :param cursor:
        :return:
        """
        cursor.close()
        conn.close()

    def execute(self, sql, args=None, commit=False):
        """
        Execute a sql, it could be with args and with out args. The usage is
        similar with execute() function in module pymysql.
        :param sql: sql clause
        :param args: args need by sql clause
        :param commit: whether to commit
        :return: if commit, return None, else, return result
        """
        print sql
        # get connection form connection pool instead of create one.
        conn = self.pool.get_connection()
        cursor = conn.cursor()
        if args:
            cursor.execute(sql, args)
        else:
            cursor.execute(sql)
        if commit is True:
            conn.commit()
            self.close(conn, cursor)#return connection to the pool
            return None
        else:
            res = cursor.fetchall()
            self.close(conn, cursor)#return connection to the pool
            return res

    def executemany(self, sql, args, commit=False):
        """
        Execute with many args. Similar with executemany() function in pymysql.
        args should be a sequence.
        :param sql: sql clause
        :param args: args
        :param commit: commit or not.
        :return: if commit, return None, else, return result
        """
        # get connection form connection pool instead of create one.
        conn = self.pool.get_connection()
        cursor = conn.cursor()
        cursor.executemany(sql, args)
        if commit is True:
            conn.commit()
            self.close(conn, cursor)
            return None
        else:
            res = cursor.fetchall()
            self.close(conn, cursor)
            return res


"""__name__ : Every module in Python has a special attribute called __name__. It is a built-in variable that returns the name of the module.
    if it runs directly like python test.py __name__ will be __main__
    if it is imported as a module, __main__ will be the module name
"""
if __name__ == "__main__":
    mysql_pool = MySQLPool(**dbconfig)
    # sql = "select * from store WHERE create_time < '2017-06-02'"
    p = Pool()
    query = "SELECT * FROM {}".format(__db_realestate_table_regions)
    # for i in range(5):
    #     res = p.apply_async(mysql_pool.execute, args=(query,))
        # print res
    print mysql_pool.execute(query, False)
    # p.apply_async(mysql_pool.execute, args=(query, ))