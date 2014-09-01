#/uer/bin/python

import MySQLdb;

#db = MySQLdb.connect('192.168.6.11:3307','okooo_php2','123465','schedule');


'''config  ={
	'host':'192.168.6.11',
	'user':'okooo_php2',
	'passwd':'123465',
	'db':'schedule',
	'port':3307,
}
'''
def py_mysql_connect(config,sql):
	try:
		db = MySQLdb.connect(**config)
		cursor = db.cursor()
		cursor.execute(sql)
	except MySQLdb.connector.Error as err:
		print("Something went wrong: {}".format(err))
	return cursor

def fetchall_result(cursor):
	data = cursor.fetchall()
	return data


#data  = cursor.fetchall();
#print data;



