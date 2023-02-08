class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        save=defaultdict(list)
        count=defaultdict(int)
        visited=set()
        lst=[]
        first=-1
        for pair in adjacentPairs:
            save[pair[0]].append(pair[1])
            save[pair[1]].append(pair[0])
            count[pair[0]]+=1
            count[pair[1]]+=1
        for num in count:
            if count[num]==1:
                first=num
                break
        lst.append(first)
        visited.add(first)
        self.dfs(first,lst,save,visited)
        return lst
    def dfs(self,num,lst,save,visited):
        
        for number in save[num]:
            if number not in visited:
                lst.append(number)
                visited.add(number)
                self.dfs(number,lst,save,visited)
        return