# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if (q is None and p is not None) or (p is None and q is not None):
            return False
        
        if p is None and q is None:
            return True
        
        
        if p.val==q.val:
            
            inp=self.isSameTree(p.left,q.left)
        
            inp2=self.isSameTree(p.right,q.right)
            
            return inp and inp2
           
            
        else:
            return False