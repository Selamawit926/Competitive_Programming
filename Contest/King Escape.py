from collections import deque

n=eval(input())
queen=input().split(" ")
king=input().split(" ")
dest=input().split(" ")
diff=[]
for i in range(len(dest)):
    diff.append(int(dest[i])-int(king[i]))

if int(king[0])<int(queen[0]) and int(dest[0])<int(queen[0]) and int(king[1])<int(queen[1]) and int(dest[1])<int(queen[1]):
    print("YES")
elif int(king[0])>int(queen[0]) and int(dest[0])>int(queen[0]) and int(king[1])>int(queen[1]) and int(dest[1])>int(queen[1]):
    print("YES")
else:
    print("NO")

# newRow=int(king[0])
# newCol=int(king[1])
# print("new: ",newRow," ",newCol)
# print(diff)




# directions=[[0,1],[1,0],[0,-1],[-1,0],[1,1],[-1,-1],[1,-1],[-1,1]]
# queue=deque()
# visited=set()
# check=False
# for direction in directions:
#     newRow=int(king[0])+direction[0]
#     newCol=int(king[1])+direction[1]
#     queue.append([newRow,newCol])
#     visited.add((newRow,newCol))

# while queue:
#     popped=queue.popleft()

#     if popped[0]==int(queen[0]) or popped[1]==int(queen[1]):
#         print("popped: ",popped)
#         check=True
#         continue

#     if popped[0]==int(dest[0]) and popped[1]==int(dest[1]):
#         print("here")
#         check=False
#         break

#     for direction in directions:
#         newRow=int(king[0])+direction[0]
#         newCol=int(king[1])+direction[1]
#         if (newRow,newCol) not in visited:
#             queue.append([newRow,newCol])
#             visited.add((newRow,newCol))
# if check:
#     print("NO")
# else:
#     print("YES")