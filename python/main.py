#!/usr/bin/env python

a = 10

def fxn():
    """ docu string is here, it does nothing
    absolutely nothing it does """
    global a
    print(a)
    a = 1
    print(a)
    # pass

# print(fxn.__doc__)

fxn()




