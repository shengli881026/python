#/usr/bin/python

class mysql_config():
	'''def __init__(self,name):
		#print 'aaaa'
		self.name = name
		print name
	'''
	def abc(self,name):
		self.name = name
		config ={
			'schedule':{
				'host':'192.168.6.11',
				'user':'okooo_php2',
				'passwd':'123465',
				'db':'schedule',
				'port':3307,
			},
		}
		return config[name]
