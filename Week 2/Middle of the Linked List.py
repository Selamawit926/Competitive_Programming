class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        
        slow=head
        fast=head
        
        while fast is not None:
            if fast.next is None:
                break
            else:
                fast=fast.next.next
                slow=slow.next
        
        
        return slow
        
        
        
#         size=0
#         actualNode=head
#         while actualNode is not None:
#             actualNode=actualNode.next
#             size+=1
            
#         if size%2!=0:
#             i=(size+1)//2
#             j=1
#             actualNode=head
#             while j!=i:
#                 j+=1
#                 actualNode=actualNode.next
                
                
#             return actualNode
        
#         else:
#             i=size//2
#             j=1
#             actualNode=head
#             while j!=i:
#                 j+=1
#                 actualNode=actualNode.next
            
#             actualNode=actualNode.next
            
#             return actualNode
        