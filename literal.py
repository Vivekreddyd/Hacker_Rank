#!/bin/python

import sys

def solve(a0, a1, a2, b0, b1, b2):
    # Complete this function
    res=[]
    alice1=0
    bob1=0
    alice1=1 if(a0>b0|a1>b1|a2>b2) else bob=0
    bob=1 if(a0<b0|a1<b1|a2<b2) else 0
    print alice1
    res=[alice1,bob]
    return res
a0, a1, a2 = raw_input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = raw_input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
print "test"
result = solve(5, 6, 7, 3, 6, 10)
print " ".join(map(str, result))