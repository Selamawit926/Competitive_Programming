# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        
        if root is None:
            root=TreeNode()
            root.val=val
            return root
        
        if val<root.val:
            if root.left is not None:
                self.insertIntoBST(root.left,val)
            else:
                root.left=TreeNode()
                root.left.val=val
                
            
        elif val>root.val:
            if root.right is not None:
                self.insertIntoBST(root.right,val)
            else:
                root.right=TreeNode()
                root.right.val=val
                
        return root