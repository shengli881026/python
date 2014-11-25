#/uer/bin/python 

import thread
import time

#print time.time()

#print t
#print time.asctime(t)


#print time.gmtime()

def get_this_time(name,s_n):
	num =0
	while num < 100:
		time.sleep(s_n)
		t =time.localtime()
		num +=1
		print name + time.strftime("%Y-%m-%d %H:%M:%S", t)
		#print name

try:
	thread.start_new_thread(get_this_time,("Thread-1",2,))
	thread.start_new_thread(get_this_time,("Thread-2",3,))
except:
	print 'except'

#get_this_time("Thread-1",1)
