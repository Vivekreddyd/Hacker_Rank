import sys
n = int(input().strip())
prev_count=0
count=0
while(n>0):
    temp=int(n)%2
    n=n/2
    if(temp==1):
        count+=1
    if(count>prev_count):
        prev_count=count
    if(temp==0):
        count=0

print (prev_count)