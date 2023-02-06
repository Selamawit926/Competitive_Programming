from collections import defaultdict
class DetectSquares:

    def __init__(self):
        self.points=defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)]+=1

    def count(self, point: List[int]) -> int:
        count=0
        for points in self.points:
            disX=abs(point[0]-points[0])
            disY=abs(point[1]-points[1])
            if disX==disY and disX>0:
                if (point[0],points[1]) in self.points and (points[0],point[1]) in self.points:
                    count+=self.points[points]*self.points[(point[0],points[1])]*self.points[(points[0],point[1])]
        return count
