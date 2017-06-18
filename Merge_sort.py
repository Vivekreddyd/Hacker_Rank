import math
arr=[6,5,3,1,8,7,2,4]

def split_arr(new_arr):
    if(len(new_arr)==2):
        if(new_arr[0]>new_arr[1]):
            new_arr[0],new_arr[1]=new_arr[1],new_arr[0]
        return new_arr
    elif(len(new_arr)==1):
        return new_arr
    split1=split_arr(new_arr[0:math.floor(len(new_arr)/2)])
    split2=split_arr(new_arr[math.floor(len(new_arr)/2)+1,len(new_arr)-1])
    merge(split1,split2)
def merge(arr1,arr2):
    i,j = 0,0
    while i>=len(arr1) and j>=len(arr2):
        if()
        i-=1
        j-=1

