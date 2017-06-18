#!/bin/python3

import sys


n1,n2,n3 = input().strip().split(' ')
n1,n2,n3 = [int(n1),int(n2),int(n3)]
h1 = [int(h1_temp) for h1_temp in input().strip().split(' ')]
h2 = [int(h2_temp) for h2_temp in input().strip().split(' ')]
h3 = [int(h3_temp) for h3_temp in input().strip().split(' ')]
temp1,temp2,temp3=[],[],[]
for i in range(0,max(len(h1),len(h2),len(h3))):
    if(h1):
        temp1.append(h1.pop(0))
    if(h2):
        temp2.append(h2.pop(0))
    if(h3):
        temp3.append(h3.pop(0))
sum1,sum2,sum3=0,0,0
h_temp1,h_temp2,h_temp3=[],[],[]
max_sum=0
for i in range(0,max(len(temp1),len(temp2),len(temp3))):
    if(temp1):
        sum1+=temp1.pop()
        h_temp1.append(sum1)
    if(temp2):
        sum2+=temp2.pop()
        h_temp2.append(sum2)
    if(temp3):
        sum3+=temp3.pop()
        h_temp3.append(sum3)
    # if(sum1==sum2 and sum1==sum3):
    #     max_sum=sum1

# print (max_sum)
final_sum=0

for i in range(0,n1+n2+n3):
    if(not h_temp1 or not h_temp2 or not h_temp3):
        break
    min_sum = min(h_temp1[-1], h_temp2[-1], h_temp3[-1])
    if(min_sum in h_temp1 and min_sum in h_temp2 and min_sum in h_temp3):
        final_sum=min_sum
        break
    else:
        while (h_temp1 and min_sum < h_temp1[-1]):
            h_temp1.pop()
        while (h_temp2 and min_sum < h_temp2[-1]):
            h_temp2.pop()
        while (h_temp3 and min_sum < h_temp3[-1]):
            h_temp3.pop()

        # if(max_sum in h_temp1):
        #     h_temp1.pop()
        # if(max_sum in h_temp2):
        #     h_temp2.pop()
        # if(max_sum in h_temp3):
        #     h_temp3.pop()
        #min_sum = min(h_temp1[-1], h_temp2[-1], h_temp3[-1])
print(final_sum)