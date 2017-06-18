# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
x=100
n=2
temp_x=x
count=0
temp_count=0
iter=math.floor(x**(1/float(n)))
#print iter
arr=[]

def check(new_x,val):
    # print val
    global temp_x
    global temp_count
    global count
    global n
    ret=False
    temp_count+=1
    if((float(new_x**(1/float(n))))==val):
        # if (new_x == temp_x):
        count = count + 1
        return True
    elif (new_x-int(val**n))>0:
        if(val-1>0):
            # ret=check((new_x-int(val**n)),val-1)
            temp=val
            while(temp-1>0):
                ret=check((new_x-int(val**n)),temp-1)
                temp-=1
            # if (new_x == temp_x and ret is True):
            #     count = count + 1
            return ret
    elif (new_x-int(val**n))<0:
        # if(new_x-int(val**n))
        return False
        # return check(new_x,math.floor(new_x**(1/float(n))))
    return False
while(iter>=1):
    check(x,iter)
    iter-=1
print temp_count
# print count