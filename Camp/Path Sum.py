# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        
        if root:
               
            if root.val==targetSum and not root.left and not root.right:
                return True
        
            if targetSum==root.val:
                return False
            
            ans=self.dfs(root,targetSum,0)
            # print(ans)
            
            return ans
                # print(ans)

        return False
        
    def dfs(self,node,targetSum,tot):
        
        tot+=node.val
        
        if tot==targetSum and not node.left and not node.right :
            return True
        
        
        leftResult=False
        rightResult=False
        
        
        if node.left:
            leftResult= self.dfs(node.left,targetSum,tot)
            # print(tot)
            
        if node.right:
          
            # print(tot)
            rightResult= self.dfs(node.right,targetSum,tot)
        
        
        
        return rightResult or leftResult