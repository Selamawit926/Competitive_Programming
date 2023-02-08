class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source==target:return 0
        save=defaultdict(list)
        for i in range(len(routes)):
            for bus in routes[i]:
                save[bus].append(i)

        queue=deque([source])
        count=0
        visited=set()
        while queue:
            count+=1
            length=len(queue)
            for i in range(length):
                curr=queue.popleft()
                for bus in save[curr]:
                    if bus not in visited:
                        visited.add(bus)
                        for currBus in routes[bus]:
                            if currBus==target: return count
                            queue.append(currBus)
        return -1
