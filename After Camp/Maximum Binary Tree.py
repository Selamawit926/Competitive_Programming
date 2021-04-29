# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        
        if len(nums)==1:
            return TreeNode(nums[0])
        
        root=TreeNode(max(nums))  
        self.recursive(root,nums)
        
        # print(root)
        return root
        
    def recursive(self,root,lst):
          
        maxi=max(lst)
        prefix=[]
        suffix=[]
        index=len(lst)-1
        for i in range(len(lst)):
            if lst[i]==maxi:
                index=i
                
            elif i>index:
                suffix.append(lst[i])
                
            else:
                prefix.append(lst[i])
                
        if prefix:
            root.left=TreeNode(max(prefix))
            self.recursive(root.left,prefix)
            
        if suffix:
            root.right=TreeNode(max(suffix))
            self.recursive(root.right,suffix)
        