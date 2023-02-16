class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        di=defaultdict(int)
        for i in changed:
            di[i]+=1
        zeros=changed.count(0)
        if zeros%2!=0:
            return []
        org=[0]*(zeros//2)
        left=zeros
        while left<len(changed):
            if di[changed[left]]>0:
                if changed[left]*2 in di and di[changed[left]*2]>0: 
                    org.append(changed[left])
                    di[changed[left]]-=1
                    di[changed[left]*2]-=1
                else:
                    return []
            left+=1
        return org
                        


        # if len(changed)%2!=0:
        #     return []
        # zeros=changed.count(0)
        # org=[]
        # if zeros%2!=0:
        #     return []
        # else:
        #     org=[0]*(zeros//2)
        # changed.sort()
        # di=defaultdict(deque)
        # for i in range(len(changed)):
        #     di[changed[i]].append(i)
        # left=zeros
        # double=set()
        # while left<len(changed):
        #     if left not in double:
        #         if changed[left]*2 in di and len(di[changed[left]*2])!=0:
        #             org.append(changed[left])
        #             double.add(di[changed[left]*2][0])
        #             di[changed[left]*2].popleft()
        #     left+=1
        # if len(org)!=len(changed)//2:
        #     return []
        # return org