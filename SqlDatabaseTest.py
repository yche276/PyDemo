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