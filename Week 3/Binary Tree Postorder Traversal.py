# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
          
        lst=[]
        
        self.addIntoList(root,lst)
        return lst
        
        
    def addIntoList(self,root,lst):
        
        if root is None:
            return
        
        
        self.addIntoList(root.left,lst)
        self.addIntoList(root.right,lst)
        lst.append(root.val)