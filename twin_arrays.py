#!/bin/python3

import sys

def twinArrays(ar1, ar2):
    # Complete this function
    min1=min(ar1)
    min2=min(ar2)
    if(ar1.index(min1)!=ar2.index(min2)):
        return min1+min2
    else:
        temp1=ar1[:]
        temp2=ar2[:]
        temp1.sort()
        temp2.sort()
        # temp1=sorted(temp1)
        # temp2=sorted(temp2)
        return min(temp1[1]+min2,temp2[1]+min1)
        '''if(temp1[1]<min2):
            return temp1[1]+min2
        else:
            return temp2[1]+min1
        if(min1<min2):
            temp=ar2[:]
            sorted(temp)
            return temp[1]+min1
        elif(min1>min2):
            temp=ar1[:]
            sorted(temp)
            return temp[1]+min2'''
n = int(input().strip())
ar1 = list(map(int, input().strip().split(' ')))
ar2 = list(map(int, input().strip().split(' ')))
result = twinArrays(ar1, ar2)
print(result)