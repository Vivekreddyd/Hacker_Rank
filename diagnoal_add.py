#!/bin/python

import sys


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)
sum1=sum2=0
for r in range(0,n):
    for c in range(0,n):
        if(r==c):
            sum1=sum1+a[r][c]
            print(r,c)
        elif(r+c==n+1):
            sum2=sum2+a[r][c]
            print(r,c)
res=abs(sum2-sum1)
print (res)