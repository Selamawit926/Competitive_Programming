# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        
        
            return self.add(root,low,high)
        
        
    def add(self,root,low,high):
        
        if root is None:
            return 0
        
        if root.val>high:
            root=root.left
            return self.add(root,low,high)
        elif root.val<low:
            root=root.right
            return self.add(root,low,high)
            
        else:
            
            inp=self.add(root.left,low,high)
            inp2=self.add(root.right,low,high)
            
        return inp+inp2+root.val
            