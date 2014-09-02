import mysql

config  ={
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
