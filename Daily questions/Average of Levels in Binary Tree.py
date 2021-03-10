# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        queue=[(root,1)]
        avg=[float(root.val)]
        level=1
        tot=0
        count=0

        while queue:
        
            node=queue.pop(0)
            
            if level!=node[1]:
                tot=tot/count
                avg.append(tot)
                tot=0
                count=0
                level=node[1]
                
            
            if node[0].left:
                queue.append((node[0].left,node[1]+1))
                tot+=node[0].left.val
                count+=1
                
            if node[0].right:
                queue.append((node[0].right,node[1]+1))
                tot+=node[0].right.val
                count+=1
                
            
            
        return avg
        