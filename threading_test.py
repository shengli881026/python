#!/uer/bin/python 

import threading
import time

class myThread(threading.Thread):
	def __init__(self,threadID,name,counter):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.counter = counter
	def run(self):
		print "----"+self.name
		get_this_time(self.name,self.counter)	
		print "****Exiting****"+self.name


def get_this_time(name,s_n):                                                                                                               
    num =0
    while num < 5:
        time.sleep(s_n)
        t =time.localtime()
        num +=1
        print name+ '-' + time.strftime("%Y-%m-%d %H:%M:%S", t)
        #print name

n=0
while n < 10:
	name = "Threading-"+str(n)
	thread_n = myThread(n,name,n)
	thread_n.start()
	n +=1
	
#thread1 = myThread(1,"Threading-1",2)
#thread2 = myThread(2,"Threading-2",3)
#thread3 = myThread(3,"Threading-3",1)
#thread1.start()
#thread2.start()
#thread3.start()
