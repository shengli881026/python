#/uer/bin/python

import MySQLdb;
from db_config import mysql_config
m_config  = mysql_config()
class db_mysql():
	def __init__(self):
		print 'class:db_mysql -import -true'

	def connect(self,name):
		#self.sql  = sql
		self.name = name
		try:
			#self.config = m_config.abc(name)
			config  = m_config.get_config(name)
			db = MySQLdb.connect(**config)
			cursor = db.cursor()
			#cursor.execute(sql)
		except MySQLdb.connector.Error as err:
			print("Something went wrong: {}".format(err))
		return cursor
	
	def execute(self,cursor,sql):
		cursor.execute(sql)
		return cursor

	def fetchall(self,cursor):
		data = cursor.fetchall()
		return data
	
	def fetchone(self,cursor):
		return cursor.fetchone()
	
	

#data  = cursor.fetchall();
#print data;



