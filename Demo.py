# python 2.7

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