#/uer/bin/python
#import db_config

#aa = db_config.db_config('schedule')
#print db_config.config_list()
#print aa;
'''config = {
        'schedule':{
        'host':'192.168.6.11',
        'user':'okooo_php2',
        'passwd':'123465',
        'db':'schedule',
        'port':3307,
        },
        }'''
import db_config

data = db_config.abc();
print data
