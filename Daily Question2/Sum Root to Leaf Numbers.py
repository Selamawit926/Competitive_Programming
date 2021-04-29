# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
    
        lst=[]
        path=""
        self.dfs(root,lst,path)
        # print(lst)
        tot=0
        for i in lst:
            tot+=int(i)
        
        return tot
        
    def dfs(self,node,lst,path):
        if not node:
            return
        
        if not node.left and not node.right:
            path+=str(node.val)
            lst.append(path)
            return
        
        path+=str(node.val)
        self.dfs(node.left,lst,path)
        self.dfs(node.right,lst,path)
        
        return
            