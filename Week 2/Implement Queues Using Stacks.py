class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1=[]
        self.stack2=[]

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        while self.size1() !=0:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(x)
        while self.size2() !=0:
            self.stack1.append(self.stack2.pop())

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.empty():
            return 
        
        return self.stack1.pop()
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.empty():
            return 
        
        return self.stack1[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stack1)==0
        
   
    def size1(self) -> int:
        return len(self.stack1)
    
    def size2(self) -> int:
        return len(self.stack2)