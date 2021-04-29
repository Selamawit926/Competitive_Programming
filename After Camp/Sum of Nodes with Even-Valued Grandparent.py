# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        di={}
        level=1
        nums=[]
        
        self.dfs(root,di,level,nums)
        return sum(nums)
        
    def dfs(self,root,di,level,nums):
        
        if not root:
            return 0
    
        di[level]=root.val
        level+=1
    
        self.dfs(root.left,di,level,nums)
        self.dfs(root.right,di,level,nums)
        
        level-=1
        if level-2>=1:
            # print(di)
            if di[level-2]%2==0: 
                nums.append(root.val)
                # print(nums)
               
        return
            