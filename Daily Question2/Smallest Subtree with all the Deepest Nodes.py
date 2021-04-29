# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        
        tree=self.dfs(root,1)
        return tree[0]
        
    def dfs(self,node,level):
        if not node:
            return
            
        if not node.left and not node.right:
            return node,level
        
        left=self.dfs(node.left,level+1
        right=self.dfs(node.right,level+1)
        
        if left and right:
            if left[1]==right[1]:
                # print(node.val,level)
                return node,left[1]
            elif left[1]>right[1]:
                return left
            else:
                return right
            
        elif left:
            return left
        
        else:
            return right