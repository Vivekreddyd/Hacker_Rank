class Node:
    def __init__(self,data,next_node=None):
        self.data=data
        self.next=next_node

class Linked_List:
    def __init__(self):
        self.head=None
counter=-1
def Read_from_last(node,pos):
    global counter
    if(not node is None):
        ret=Read_from_last(node.next,pos)
        counter+=1
        if(counter==pos):
            return node.data
        if(not ret is None):
            return ret
    return None
head=None
input_arr=[1,2,3,4,5,6]
for i in range(0,len(input_arr)):
    if(i==0):
        head=Node(input_arr[i])
        # head.data=input_arr[i]
        prev=head
    else:
        temp=Node(input_arr[i])
        # temp.data=input_arr[i]
        prev.next=temp
        prev=temp
curr=head
for i in range(0,len(input_arr)):
    print curr.data
    curr=curr.next
position=3

data=Read_from_last(head,position)
print data