class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        tos=defaultdict(list)
        vert=[]
        for edge in edges:
            tos[edge[1]].append(edge[0])
        for i in range(n):
            if i not in tos:
                vert.append(i)
        return vert
