n=int(input())
dict_nodes={}
#dict_nodes[1]=1
for i in range(0,n):
    a,b=input().split(" ")
    dict_nodes[i+1]=[a,b]
T=int(input())
# tt=input()
# print(tt)
# n=11
# dict_nodes={}
# dict_nodes[1]=[2,3]
# dict_nodes[2]=[4,-1]
# dict_nodes[3]=[5,-1]
# dict_nodes[4]=[6,-1]
# dict_nodes[5]=[7,8]
# dict_nodes[6]=[-1,9]
# dict_nodes[7]=[-1,-1]
# dict_nodes[8]=[10,11]
# dict_nodes[9]=[-1,-1]
# dict_nodes[10]=[-1,-1]
# dict_nodes[11]=[-1,-1]
# dict_nodes[12]=[-1,-1]
# dict_nodes[13]=[-1,-1]
# dict_nodes[14]=[-1,-1]
# dict_nodes[15]=[-1,-1]
# dict_nodes[16]=[-1,-1]
# dict_nodes[17]=[-1,-1]
# T=2
# k_val=[2,4]

def Inorder(cur):
    global dict_nodes
    left=int(dict_nodes[cur][0])
    right=int(dict_nodes[cur][1])
    if(left!=-1):
        Inorder(left)
    print ((cur),end=" ")
    if(right!=-1):
        Inorder(right)

for j in range(1,T+1):
    k_val=int(input())
    # k=k_val[j-1]
    rep=1
    test=True
    while(test):
        k=rep*k_val
        arr_temp=[]
        arr_new=[1]
        for depth in range(0,k-1):
            #iter_val=0
            arr_temp=arr_new[:]
            arr_new=[]
            while(arr_temp):
                #iter_val+=1
                val=int(arr_temp.pop())
                if(val!=-1):
                    new=dict_nodes[val]
                    for x in range(0,2):
                        arr_new.append(int(new[x]))
                #print (arr_new)
                #if(iter_val)
        if((len(set(arr_new))==1 and arr_new[0]==-1)or not arr_new):
            test=False
            Inorder(1)
            print("")
            break

        for val1 in arr_new:
            #print (val1)
            if(int(val1)!=-1):
                temp=dict_nodes[int(val1)]
                #temp[0],temp[1]=temp[1],temp[0]
                #count=1
                dict_nodes[int(val1)]=[temp[1],temp[0]]
        rep+=1
    #print (dict_nodes)
    #arr_temp=[j]
    #k=j
    #while(arr_temp):
        #temp=dict_nodes[k]
        #arr_temp.append(temp[i] for i in range(0,2))
        #k=arr_temp.pop(0)