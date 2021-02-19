"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        # print(root.children)
        if not root:
            return 0
        
        if root.children:
            return self.dfs(root)
        
    
        else:
            return 1
    

    def dfs(self,root):
        maxi=0
        if len(root.children)==0:
            return 1
        
        for i in root.children:
            
            maxiu=self.dfs(i)
            
            if maxiu>maxi:
                maxi=maxiu
                
        return maxi+1