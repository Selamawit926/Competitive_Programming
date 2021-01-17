def findMergeNode(head1, head2):
    
    stack1=[]
    stack2=[]
    currentNode1=head1
    currentNode2=head2
    
    while currentNode1 is not None:
        stack1.append(currentNode1)
        currentNode1=currentNode1.next
    
    while currentNode2 is not None:
        stack2.append(currentNode2)
        currentNode2=currentNode2.next
        
    z=None
    for i in range(0,len(stack2)):
        if len(stack1)==0 or len(stack2)==0:
            break
        
        x=stack1.pop()
        y=stack2.pop()
        
        if x==y:
            z=x.data
        else:
            break
        
    return z