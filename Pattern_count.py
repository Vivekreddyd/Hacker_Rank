#!/bin/python3

import sys
import re


def patternCount(s):
    # Complete this function
    s1=s.replace('1', '11')
    pat = re.compile('10+1')
    mat = pat.findall(s1)

    # mat1=pat.match(s)
    # print (mat1.groups().count())
    # coun1=mat.findall
    return (len(mat))


q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = patternCount(s)
    print(result)
