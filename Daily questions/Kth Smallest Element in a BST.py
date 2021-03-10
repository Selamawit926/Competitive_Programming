# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        
        heap=[]
        
        self.findAll(root,heap)
        # print(heap)
        heapq.heapify(heap)
        
        for i in range(k):
            kth=heapq.heappop(heap)
            
        # print(kth)
        return kth
            
    def findAll(self,node,lst):
        
        lst.append(node.val)
        if node.left:
            self.findAll(node.left,lst)
        if node.right:
            self.findAll(node.right,lst)
        
        return