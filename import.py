#/usr/bin/python
# -*- coding: latin-1 -*-


#类的外部调用两种方法
#-----------import-----------------
import db_config
#db_config  导入文件的名称
#mysql_config 类的名称 因为类也是一个方法
#abc() mysql_config 中类的
db_config.mysql_config().abc();
#-----------import end-------------


#---------from module import--------
from db_config import mysql_config
#1 直接访问
mysql_config().abc();
#2 实例化访问
obj = mysql_config();
obj.abc();
#---------end from module import----


#---------import 和 from module import 区别----------------
#import  直接导入当前文件
#from types<文件名称> import FunctionType<方法名称>

#如果你要经常访问模块的属性和方法，且不想一遍又一遍地敲入模块名，使用 from module import。
#如果你想要有选择地导入某些属性和方法，而不想要其它的，使用 from module import。
#如果模块包含的属性和方法与你的某个模块同名，你必须使用 import module 来避免名字冲突。

#-----------------------------------------------------------
'''config = {
        'schedule':{
        'host':'192.168.6.11',
        'user':'okooo_php2',
        'passwd':'123465',
        'db':'schedule',
        'port':3307,
        },
        }'''


#import db_config
#from db_config import *

#obj_mysql_config = mysql_config();

#obj_mysql_config.abc();
#db_config.db_config().abc();

