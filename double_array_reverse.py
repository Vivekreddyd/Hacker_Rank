class Node(object):
    def __init__(self, data=None, next_node=None, prev_node=None):
        self.data = data
        self.next = next_node
        self.prev = prev_node


def Reverse(head):
    if(head is None):
        return head
    else:
        current=head.next
        head.next=None
        previous=head
        while(not current is None):
            temp=current.next
            current.next=previous
            current.next.prev=current
            previous=current
            current=temp
        head=previous
        head.prev=None
        return head
arr1=[6,4,2]
for i in range(0,len(arr1)):
    if(i==0):
        head=Node(arr1[i],None,None)
        previous=head
    else:
        temp=Node(arr1[i],None,previous)
        previous.next=temp
        previous=temp


head=Reverse(head)
current=head
while not current is None:
    print current.data
    current=current.next