class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        
        lst=[0]*(max(A)+1)
        lst2=[]

        for i in A:
            lst[i]+=1


        for i in range(0,len(lst)):
            for k in range(0,lst[i]):
                lst2.append(i) 
        
        x=0
        for i in range(len(lst2)-1,1,-1):
            if lst2[i]+lst2[i-1]>lst2[i-2] and lst2[i]+lst2[i-2]>lst2[i-1] and lst2[i-1]+lst2[i-2]>lst2[i]:
                x+=1
                return lst2[i]+lst2[i-1]+lst2[i-2]
                break

                    
        if x==0:
            return 0
            


                