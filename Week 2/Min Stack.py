class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]
        self.storeMin=[]
        

    def push(self, x: int) -> None:
        if len(self.stack)==0:
            self.storeMin.append(x)
        else:
            if x<=self.storeMin[-1]:
                self.storeMin.append(x)
        self.stack.append(x)

    def pop(self) -> None:
        if self.stack.pop()==self.storeMin[-1]:
            self.storeMin.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if len(self.storeMin)==0:
            return
        return self.storeMin[-1]