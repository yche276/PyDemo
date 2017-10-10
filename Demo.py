# python 2.7
# import MySQLdb as mdb
import sys
import Queue
import threading
import urllib2

from multiprocessing.dummy import Pool as ThreadPool


print 'Hello Python World'

x = set('abcde')
y = set('bdxyz')
print x
print y


# print(sys.platform)
# print(2 ** 100)
# x = 'Spam!'
# print(x * 8)
#
# # test commit
# globvar = 0
#
# def set_globvar_to_one():
#     global globvar    # Needed to modify global copy of globvar
#     globvar = 1
#
# def print_globvar():
#     print(globvar)     # No need for global declaration to read value of globvar
#
# set_globvar_to_one()
# print_globvar()       # Prints 1
#
#
# list1 = [2, 3, 5, 7, 11, 13, 17, 19]
# mean = 0.0
# for i in list1:
#     mean = mean + i
# mean /= len(list1)
#
# print ('list1 = %s' % list1)
# print (mean)
# print ('mean = %f, aaaa = %d' % (mean, 10))

# tests

"""
#
worker_data = ['http://google.com', 'http://yahoo.com', 'http://bing.com']


#load up a queue with your data, this will handle locking
q = Queue.Queue()
for url in worker_data:
    q.put(url)


#define a worker function
def worker(queue):
    queue_full = True
    while queue_full:
        try:
            #get your data off the queue, and do some work
            url= queue.get(False)
            data = urllib2.urlopen(url).read()
            print len(data)

        except Queue.Empty:
            queue_full = False

#create as many threads as you want
thread_count = 5
for i in range(thread_count):
    t = threading.Thread(target=worker, args = (q,))
    t.start()

"""


