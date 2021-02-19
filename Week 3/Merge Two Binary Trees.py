# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        
        if not root1 and not root2:
            return 
        
        if root1 and root2:
        
            root1.val=root1.val+root2.val

            if root1.left and root2.left:
                self.mergeTrees(root1.left,root2.left)
            elif root2.left and not root1.left:
                root1.left=root2.left
            if root1.right and root2.right:
                self.mergeTrees(root1.right,root2.right)

            elif  root2.right and not root1.right:
                root1.right=root2.right


            return root1
        
        elif root1:
            return root1
        
        else:
            return root2