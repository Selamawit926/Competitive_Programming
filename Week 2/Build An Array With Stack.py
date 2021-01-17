class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        
        lst=[]
        arr=[]
        for i in range(1,n+1):
            if len(lst)==len(target):
                break
            lst.append(i)
            arr.append("Push")
            # print(lst[i])
            j=len(lst)-1
            if lst[j]!=target[j]:
                lst.pop()
                # print(len(lst))
                arr.append("Pop")
            
        return arr