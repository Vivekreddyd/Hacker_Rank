arr=[6,5,3,1,8,7,2,4]

for i in range(0,len(arr)-1):
    if(arr[i]>arr[i+1]):
        j=i
        temp=arr[i+1]
        while(j>=0):
            if(arr[j]>temp):
                arr[j],arr[j+1]=arr[j+1],arr[j]
            else:
                break
            j -= 1