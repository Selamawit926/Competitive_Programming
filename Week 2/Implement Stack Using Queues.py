class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1=[]
        self.queue2=[]

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue1.append(x)
        while self.size1() !=0:
            self.queue2.insert(0,self.queue1.pop())
        
    
    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.empty():
            return
        return self.queue2.pop(0)

    def top(self) -> int:
        """
        Get the top element.
        
        """
        if self.empty():
            return
        
        return self.queue2[0]
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.queue2)==0
    
    
    def size1(self) -> int:
        return len(self.queue1)