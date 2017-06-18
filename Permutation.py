
perm=['a','b','c','d']
com_arr=[]
# while(True):
for i in range(0,len(perm)):
    j=0
    while(j+i+1<=len(perm)):
    #for j in range(0,len(perm)):
        temp=perm[j:j+i+1]
        j+=1
        com_arr.append(temp)
# com_arr=[' '.join(i) for i in itertools.product(perm,repeat=3)]
# # for i in range(0,len(perm)):
# #     com_arr.append(perm[i])
# #     com_arr.append([perm[i])
# print com_arr