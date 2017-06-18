import sys
spush=['{','[','(']
spop=['}',']',')']

t = int(input().strip())
for a0 in range(t):
    s = input().strip()
    arr=[]
    for i in range(0,len(s)):
        if(s[i] in spush):
            arr.append(s[i])
        # elif(str(arr[-1])==str(s[i])):
        #     arr.pop()
        #     continue
        else:
            temp=str(arr.pop())
            if((temp=='(' and s[i]==')')or(temp=='{' and s[i]=='}')or(temp=='[' and s[i]==']')):
                continue
            else:
                break
    if(not arr):
        print ("YES")
    else:
        print ("NO")