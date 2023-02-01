class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # count=left=right=blacks=0
        # mini=float("inf")
        # while left<=len(blocks)-k:
        #     if blacks==k:
        #         mini=min(count,mini)
        #         count=blacks=0
        #         left+=1
        #         right=left
        #         if left>len(blocks)-k:break
        #     if blocks[right]=="W":
        #         count+=1
        #     right+=1
        #     blacks+=1
        # return mini
        left=right=whites=0
        mini=float("inf")
        while right<len(blocks):
            if blocks[right]=="W":
                whites+=1
            if (right-left)+1==k:
                mini=min(mini,whites)
                if blocks[left]=="W":whites-=1
                left+=1
            right+=1
        return mini