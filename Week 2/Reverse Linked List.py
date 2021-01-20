class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
              
        #Done recursively 
        if head is None:
            return
        
        if head.next is None:
            return head
        
        
        fakeTail=self.reverseList(head.next)
        head.next.next=head
        head.next.next.next=None
        
        
        
    
        
        return fakeTail
        
    
        #Done iteratively
        actualNode=head
        previousNode=None
        newNode=None
        
        while actualNode is not None:
            newNode=actualNode.next
            actualNode.next=previousNode
            previousNode=actualNode
            actualNode=newNode
            
        
            
        return previousNode