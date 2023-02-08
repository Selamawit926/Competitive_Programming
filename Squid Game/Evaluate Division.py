class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph=defaultdict(list)
        lst=[]
        for i in range(len(equations)):
            graph[equations[i][0]].append((equations[i][1],1/values[i]))
            graph[equations[i][1]].append((equations[i][0],values[i]))
        for query in queries:
            visited=set()
            if query[0] not in graph or query[1] not in graph:
                lst.append(-1)
                continue
            if query[0]!=query[1]:
                lst.append(1/self.helper(query[0],query[1],1,graph,visited))
            else:
                lst.append(1)
        return lst
    
    def helper(self,first,second,num,graph,visited):
        if first==second: return num
        visited.add(first)
        if first in graph:
            for i in graph[first]:
                if i[0] not in visited:
                    curr=self.helper(i[0],second,num*i[1],graph,visited)
                    if curr!=-1: return curr
        return -1