# python 2.7
import MySQLdb as mdb
import sys

print 'Hello World'
print(sys.platform)
print(2 ** 100)
x = 'Spam!'
print(x * 8)

# test commit
globvar = 0

def set_globvar_to_one():
    global globvar    # Needed to modify global copy of globvar
    globvar = 1

def print_globvar():
    print(globvar)     # No need for global declaration to read value of globvar

set_globvar_to_one()
print_globvar()       # Prints 1


list1 = [2, 3, 5, 7, 11, 13, 17, 19]
mean = 0.0
for i in list1:
    mean = mean + i
mean /= len(list1)

print ('list1 = %s' % list1)
print (mean)
print ('mean = %f, aaaa = %d' % (mean, 10))

