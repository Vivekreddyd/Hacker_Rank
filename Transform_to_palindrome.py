#!/bin/python3

import sys
def find(t,val):
    for row,i in enumerate(t):
        try:
            col=i.index(val)
        except ValueError:
            continue
        return row
    return -1
arr=[[]]
i=0
n,k,m = input().strip().split(' ')
n,k,m = [int(n),int(k),int(m)]
for a0 in range(k):
    x,y = input().strip().split(' ')
    x,y = [int(x),int(y)]
    if(x in arr or y in arr):
        index1=find(arr, x)
        if(index1==-1):
            index1=find(arr,y)
            arr[index1].append(x)
        arr[index1].append(y)
        #print("nothing")
    else:
        arr[i].extend((x,y))
        i+=1
a = list(map(int, input().strip().split(' ')))
