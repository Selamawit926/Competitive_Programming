from typing import Optional



# @lc app=leetcode id=222 lang=python3
#
# [222] Count Complete Tree Nodes
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        count=1
        for i in range(len(root)):
            if (2*i)+1< len(root):
                count+=1
            else:
                return count
            if(2*i)+2<len(root):
                count+=1
            else:
                return count

        return count
            


# @lc code=end

