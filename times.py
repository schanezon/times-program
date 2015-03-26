#!/usr/bin/env python
import sys

def f(n, a):
    return n*a
if len(sys.argv) <3:
    print 'Please put 2 arguments'
else:
    print f(int(sys.argv[1]), int(sys.argv[2]))
