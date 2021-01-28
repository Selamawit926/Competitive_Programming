# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        
        if root is None:
            return 
        
        if val==root.val:
            return root
        
        elif val > root.val:
            root=root.right
            return self.searchBST(root,val)
            
        elif val<root.val:
            root=root.left
            return self.searchBST(root,val)