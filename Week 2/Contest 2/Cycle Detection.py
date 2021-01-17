def has_cycle(head):
    
    slow=head
    fast=head.next
    
    while slow!=fast:
        if fast is None or fast.next is None:
            return 0
        slow=slow.next
        fast=fast.next.next
        
    return 1