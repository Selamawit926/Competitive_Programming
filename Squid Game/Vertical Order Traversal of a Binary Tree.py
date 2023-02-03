# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        lstD=defaultdict(list)
        queue=[[root,0]]
        while queue:
            node=defaultdict(list)
            currQ=[]
            for i in range(len(queue)):
                currNode=queue[i][0]
                col=queue[i][1]
                node[col].append(currNode.val)
                if currNode.left:
                    currQ.append([currNode.left,col-1])
                if currNode.right:
                    currQ.append([currNode.right,col+1])
            for i in node:
                lst=node[i]
                lst.sort()
                for j in lst:
                    lstD[i].append(j)
            queue=currQ

        outputD=sorted(lstD)
        output=[]
        for i in range(len(outputD)):
            output.append(lstD[outputD[i]])
        return output