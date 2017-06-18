class Node:
    def __init__(self,data=None,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right


def print_tree(root, pos):

    print root

def lca(root , v1 , v2):
    #Enter your code here
    if(not root is None):
        left=lca(root.left,v1,v2)
        right=lca(root.right,v1,v2)
        if(left==True and right==True):
            return root
        # elif(left==True or right==True):
        #     return True
        elif (left is True or right is True):
            if (root.data == v1 or root.data == v2):
                return root
            else:
                return True
        elif(not left is None and right is None):
            return left
        elif(left is None and not right is None):
            return right


        if (root.data == v1 or root.data == v2):
            return True

    return None


def insert(r,val):
    #Enter you code here.
    if(r is None):
        temp=Node(val)
        temp.left=None
        temp.right=None
        r=temp
    elif(r.data<val):
        if(not r.right is None):
            r.right=insert(r.right,val)
        else:
            temp=Node(val)
            #temp.data=val
            r.right=temp
    else:
        if(not r.left is None):
            r.left=insert(r.left,val)
        else:
            temp=Node(val)
            #temp.data=val
            r.left=temp
    return r

arr=[23,16,15,9,6,17,10,13,8,26,18,2,22,24,12,5,20,21,4,19,1,3,14,7]
head=Node(25)
for i in arr:
    head=insert(head,i)
# cur=head
# arr=[head]
# arr_len=[18]
# c=20
# x=20
# print " "*c+str(head.data)
# i=1
# while(arr):
#     # if(i==2):
#     #     i=1
#     c=arr_len.pop(0)
#     # temp=c-i
#     cur=arr.pop(0)
#     if (not cur.left is None or not cur.right is None):
#         # print ""
#         print " "*c,
#     if(not cur.left is None):
#         arr.append(cur.left)
#         arr_len.append(c-2)
#         # arr_len()
#         print str(cur.left.data),
#     if (not cur.right is None):
#         arr.append(cur.right)
#         arr_len.append(c+2)
#         print ' '+str(cur.right.data)
#     # i+=1
#
ret=lca(head,23,3)
print ret.data