#/usr/bin/python/

from mysql import db_mysql

mysql_obj = db_mysql()

sql ="SELECT * FROM `bet_match` WHERE `match_id` = '610435' LIMIT 10";
cursor_connect  = mysql_obj.connect('schedule')
cursor_execute  = mysql_obj.execute(cursor_connect,sql)
data 			= mysql_obj.fetchall(cursor_execute)

#data  = mysql_obj.fetchall_result(cursor)
print data;


















#import mysql

'''config  ={
    'host':'192.168.6.11',
    'user':'okooo_php2',
    'passwd':'123465',
    'db':'schedule',
    'port':3307,
}
sql ="SELECT * FROM `bet_match` WHERE `match_id` = '610435' LIMIT 10"
obj = mysql.py_mysql_connect(config,sql)
data = mysql.fetchall_result(obj)
print data;
'''
