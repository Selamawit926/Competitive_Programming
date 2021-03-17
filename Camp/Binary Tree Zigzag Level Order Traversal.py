# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if root:
            
            queue=[(root,1)]
            levels=[]
            
            
            
            while queue:
                
                node=queue.pop(0)
                
                if len(levels)==node[1]:
                    if node[1]%2==0:
                        
                        levels[node[1]-1].insert(0,node[0].val)
                    
                    else:
                        levels[node[1]-1].append(node[0].val)
                        
                else:
                    levels.append([node[0].val])
                    
                    
                
                if node[0].left:
                    queue.append((node[0].left,node[1]+1))
                    
                if node[0].right:
                    queue.append((node[0].right,node[1]+1))
                

                        
                        
            return levels
                        
                
                    
        return []     