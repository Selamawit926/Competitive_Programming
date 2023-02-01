class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k==1:
            return head
        
        length=0
        current=head
        while current:
            current=current.next
            length+=1
            
        current=head
        start=head
        count=0
        begin=None
        times=1
        while length-count>=k:
            cnt=0
            while cnt<k:
                current=current.next
                cnt+=1
            cnt=0
            curr=current
            while cnt<k:
                node=start
                start=start.next
                node.next=curr
                curr=node
                cnt+=1
            # print("curr",curr,"with",current)
            if count==0:
                begin=curr
            else:
                node=begin
                cnt=0
                while cnt<(times*k)-1:
                    node=node.next
                    cnt+=1
                node.next=curr
                times+=1
            count+=k
        return begin



       