import numpy as np
# x,y=4,4;
# arr=np.array([[0 for x in range(x)] for y in range(y)], np.int32)
arr=[[0,1,0,1,0],[0,1,1,1,0],[0,0,0,0,0],[0,1,1,1,1]]
node=[[0]*len(arr[0]) for i in range(0,len(arr))]
print len(arr)
print len(arr[0])
# arr=np.array([[0,1,0,1,0,1],[0,1,1,1,0],[0,0,0,0,0],[0,1,1,1,1]], np.int32)
# print arr
count_var=0
def connect(i,j):
    global count_var
    if (i in range(0,len(arr)) and j in range(0,len(arr[0]))):
        if (arr[i][j]==1 and node[i][j]==0):
            count_var += 1
            node[i][j]=1
            connect(i+1,j)
            connect(i,j+1)
            connect(i+1,j+1)
            connect(i-1,j)
            connect(i,j-1)
            connect(i-1,j-1)
            connect(i-1,j+1)
            connect(i+1,j-1)

for i in range(0,len(arr)):
    for j in range(0,len(arr[0])):
        # global count_var
        count_var=0
        connect(i,j)
        print(str(i)+','+str(j)+'='+str(count_var))
        # print("%fi and %fj connected count: %fcount"%i%j%count)