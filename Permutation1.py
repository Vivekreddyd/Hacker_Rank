perm=['a','b','c','d']
com_arr=[]
# while(True):
def rec(arr1,arr2):
    temp_arr1=[]
    if arr2:
        for i in arr2:
            temp_arr1=arr1+list(i)
            temp=arr2[:]
            temp.remove(i)
            rec(temp_arr1,temp)

            #print arr1
    else:
        print arr1
for i in range(0,len(perm)):
    j=0
perm=['a','b','c','d']
com_arr=[]
# while(True):
for i in perm:
    perm1=perm[:]
    perm1.remove(i)
    new_arr=[i]
    rec(new_arr,perm1)
# for i in range(0,len(perm)):
#     j=0
#     while(j+i+1<=len(perm)):
#     #for j in range(0,len(perm)):
#         temp=perm[j:j+i+1]
#         j+=1
#         com_arr.append(temp)
# com_arr=[' '.join(i) for i in itertools.product(perm,repeat=3)]
# # for i in range(0,len(perm)):
# #     com_arr.append(perm[i])
# #     com_arr.append([perm[i])
# print com_arr
#     while(j+i+1<=len(perm)):
#     #for j in range(0,len(perm)):
#         temp=perm[j:j+i+1]
#         j+=1
#         com_arr.append(temp)
# com_arr=[' '.join(i) for i in itertools.product(perm,repeat=3)]
# # for i in range(0,len(perm)):
# #     com_arr.append(perm[i])
# #     com_arr.append([perm[i])
# print com_arr