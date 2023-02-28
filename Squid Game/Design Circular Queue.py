class MyCircularQueue:

    def __init__(self, k: int):
        self.k=k
        self.lst=[0]*self.k
        self.front=-1
        self.rear=-1
        # print(self.lst)
    def enQueue(self, value: int) -> bool:
        # print(self.rear)
        if self.isEmpty():
            self.front=0
        elif self.isFull():
            return False
        if self.rear==self.k-1 and self.front!=0:
            self.rear=-1
        # print(self.rear)  
        self.lst[self.rear+1]=value
        print(self.lst)
        self.rear+=1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.lst[self.front]=0
        if self.front+1 != self.rear+1:
            if self.front+1 == self.k:
                self.front=0
            else:
                self.front+=1
        else:
            self.front=self.rear=-1
        
        return True
       
    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.lst[self.front]
    
    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.lst[self.rear]

    def isEmpty(self) -> bool:
        if self.rear==-1 and self.front==-1:
            return True
        return False
    
    def isFull(self) -> bool:
        if self.rear==self.k-1 and self.front==0:
            return True
        
        if self.front==self.rear+1:
            return True
        
        return False