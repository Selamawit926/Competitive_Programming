class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
    
        carry=0
        head=l3=ListNode()
        
        
        while l1 is not None or l2 is not None:
            
            if l1 is None:
                l1=ListNode()
                
            elif l2 is None:
                l2=ListNode()
                
           
            tot= l1.val+l2.val+carry
        
            
            l1=l1.next
            l2=l2.next
            l3.val=tot%10
            carry=tot//10
        

            if l1 is not None or l2 is not None:
                l3.next=ListNode()
                l3=l3.next

     
        if carry==1:
            l3.next=ListNode(carry)
            
            
        return head