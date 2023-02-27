class NestedIterator:
#     def __init__(self, nestedList: [NestedInteger]):
#         self.nestedList=nestedList
#         self.index=0
#         self.temp=[]
#         self.listDone=True
#         self.listIndex=0
        
#     def next(self) -> int:
#             if self.nestedList[self.index].isInteger():
#                 num=self.nestedList[self.index].getInteger()
#                 self.index+=1
#                 return num
#             else:
#                 if self.listDone:
#                     if len(self.nestedList[self.index].getList())>0:
#                         print(self.nestedList[self.index].getList())
#                         self.addToList(self.nestedList[self.index])
#                         self.listDone=False
#                         num=self.temp[0]
#                         if self.listIndex+1<len(self.temp):
#                             self.listIndex+=1
#                         else:
#                             self.listDone=True
#                             self.index+=1
#                             self.temp=[]
#                             self.listIndex=0
#                         return num
#                     else:
#                         self.index+=1
                     
#                 else:
#                     num=self.temp[self.listIndex]
#                     if self.listIndex+1<len(self.temp):
#                         self.listIndex+=1
#                     else:
#                         self.listDone=True
#                         self.temp=[]
#                         self.listIndex=0
#                         self.index+=1
#                     return num
                    
#     def hasNext(self) -> bool:
#          return self.index<len(self.nestedList)
        
#     def addToList(self,lst):
#         lst=lst.getList()
#         for i in lst:
#             if i.isInteger():
#                 self.temp.append(i.getInteger())
                
#             else:
#                 self.addToList(i)
#         return
    def __init__(self, nestedList):
        self.stack = [[nestedList, 0]]

    def next(self):
        self.hasNext()
        nestedList, i = self.stack[-1]
        self.stack[-1][1] += 1
        return nestedList[i].getInteger()
            
    def hasNext(self):
        s = self.stack
        while s:
            nestedList, i = s[-1]
            if i == len(nestedList):
                s.pop()
            else:
                x = nestedList[i]
                if x.isInteger():
                    return True
                s[-1][1] += 1
                s.append([x.getList(), 0])
        return False