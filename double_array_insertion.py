
 # Insert a node into a sorted doubly linked list
 # head could be None as well for empty list
 # Node is defined as

class Node(object):

    def __init__(self, data=None, next_node=None, prev_node = None):
       self.data = data
       self.next = next_node
       self.prev = prev_node


def SortedInsert(head, data):
    if head.data is None:
        temp = Node
        temp.data = data
        temp.next = None
        temp.prev = None
        head = temp
        # print (head.data)
    else:
        current = head
        # prev=head
        while (not current is None):
            if (data < current.data):
                temp = Node(data)
                #temp.data = data
                # if (current.next is None):
                #     temp.next = None
                # else:
                temp.next=current
                    # temp.next=current.next
                if (not current.prev is None):
                    temp.prev = current.prev
                    current.prev.next = temp
                    current.prev=temp
                else:
                    current.prev = temp
                if (current is head):
                    temp.prev=None
                    head = temp
                break
            elif (current.next is None):
                temp = Node(data)
                #temp.data = data
                temp.prev=current
                temp.next=None
                current.next=temp
                break
            current = current.next
            # if(current.next is None):
    return head

arr1=[2,1,4,3]
arr2=[1,4,2,3,7,6,9,10]
head=Node(None)
for i in arr2:
    head=SortedInsert(head,i)
    cur=head
    while(not cur is None):
        print cur.data
        cur=cur.next