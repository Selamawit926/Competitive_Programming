class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        directions={"N":["E","W"],"E":["S","N"],"S":["W","E"],"W":["N","S"]}
        curr=[0,0]
        direction="N"
        for instruction in instructions:
            if instruction=="G":
                if direction=="N":
                    curr[1]+=1
                elif direction=="S":
                    curr[1]-=1
                elif direction=="W":
                    curr[0]-=1
                else:
                    curr[0]+=1
            elif instruction=="L":
                direction=directions[direction][1] 
            else:
                direction=directions[direction][0]
        return curr==[0,0] or direction!="N"