#!/bin/python3

import sys

g = int(input().strip())


def max_count(a_cur, b_cur, sum_cur):
    global x, a, b,n,m
    if (sum_cur > x):
        return 0
    else:
        if(a_cur < n-1):
            l_count = max_count(a_cur + 1, b_cur, sum_cur + a[a_cur + 1])
        else:
            l_count=0
        if (b_cur < m-1):
            r_count = max_count(a_cur, b_cur + 1, sum_cur + b[b_cur + 1])
        else:
            r_count=0
        l_count += 1
        r_count += 1
        return l_count if (l_count > r_count) else r_count


for a0 in range(g):
    n, m, x = input().strip().split(' ')
    n, m, x = [int(n), int(m), int(x)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    # your code goes here
    l = max_count(0, -1, a[0])
    r = max_count(-1, 0, b[0])
    if(l>r):
        print(l)
    else:
        print(r)