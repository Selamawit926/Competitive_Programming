"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
         
        visited=set()
        ans=self.dfs(id,employees,0,visited)
        return ans
    
    
    def dfs(self,target,employees,tot,visited):
        
        for i in range(len(employees)):
            if employees[i].id==target:
                if employees[i].id not in visited:
                    visited.add(employees[i].id)
                    tot=tot+employees[i].importance
                    for j in range(len(employees[i].subordinates)):
                        tot=self.dfs(employees[i].subordinates[j],employees,tot,visited)
                    
        
            
        return tot