class Node(object):
     def __init__(self,val):
            self.val=val
            self.next=None
            
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head=None
        self.size=0
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        actualNode=self.head
        if index>=self.size:
            return -1
        else:
            i=0
            while i!=index:
                actualNode=actualNode.next
                i+=1
       
            return actualNode.val
    

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        newNode=Node(val)
        self.size+=1
        if not self.head:
            self.head=newNode
            
        else:
            newNode.next=self.head
            self.head=newNode

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        
        newNode=Node(val)
        if self.size==0:
            self.head=newNode
            self.size+=1
        else:   
            actualNode=self.head
            self.size+=1
            
            while actualNode.next is not None:
                actualNode=actualNode.next
                
            actualNode.next=newNode
            newNode.next=None

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        newNode=Node(val)
        actualNode=self.head
        previousNode=None
#         i=0
#         if i==self.size-1:
#             while actualNode.next is not None:
#                 actualNode=actualNode.next
            
#             actualNode.next=newNode
#             newNode.next=None
           
        if index==0:
            newNode.next=self.head
            self.head=newNode
            self.size+=1
    
        elif index==self.size:
            actualNode=self.head
            while actualNode.next is not None:
                actualNode=actualNode.next
                    
            actualNode.next=newNode
            newNode.next=None
            self.size+=1
        elif index <self.size:
            i=0
            while i!= index:
                previousNode=actualNode
                actualNode=actualNode.next
                i+=1
                
            
            newNode.next=actualNode
            previousNode.next=newNode
           
        
        
            self.size+=1
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        i=0
        if self.head is None:
            return

        if index==0:
            self.head=self.head.next
            self.size-=1
            
        elif index<self.size:  
            actualNode=self.head
            previousNode=None
            while i!=index:
                previousNode=actualNode
                actualNode=actualNode.next
                i+=1
                
            
            previousNode.next=actualNode.next
            self.size-=1

    def traverse(self):
        actualNode=self.head
        while actualNode is not None:
            print("%d" % actualNode.val, end = " ")
            actualNode= actualNode.next

    def getSize(self):
        print(self.size)

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(1)
# obj.addAtHead(2)
# obj.addAtHead(1)

# obj.traverse()
# obj.deleteAtIndex(2)
# obj.traverse()
# obj.addAtHead(6)
# obj.traverse()
# obj.addAtTail(3)
# obj.traverse()
# obj.getSize()
# obj.get(4)
# obj.traverse()
# obj.addAtHead(4)
# obj.traverse()

# obj.addAtIndex(0,10)

# obj.addAtIndex(0,20)
# obj.addAtTail(1)

# obj.getSize()
# obj.addAtIndex(1,30)
# obj.traverse()
# obj.get(0)

# obj.addAtHead(6)
# obj.getSize()
# obj.traverse()

# obj.addAtHead(1)
# obj.addAtTail(3)
# obj.addAtIndex(1,2)
# obj.traverse()
# obj.get(1)
# obj.deleteAtIndex(1)
# obj.traverse()
# obj.get(0)
# obj.traverse()