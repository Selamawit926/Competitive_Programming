# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        if root is None:
            return True
        
        return self.check(root.left,root.right)
        
        
        
    
    def check(self,left,right):
        
        if left is None and right is None:
            return True
        
        if (left is None and right is not None) or left is not None and right is None:
            return False
        
        
        if left.val==right.val:
            inp1=self.check(left.left,right.right)
            inp2=self.check(left.right,right.left)
            
            # print(left.val,right.val,inp1 and inp2)
            return inp1 and inp2
            
            
        else:
            return False
    
        