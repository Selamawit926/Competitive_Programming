# def check(red,blue,nums,forRed,forBlue,i,visited,scores):
#     for j in range(nums):
#         if j not in visited: 
#             forRed.append(red[j])
#             forBlue.append(blue[j])
#             visited.add(j)
#             scores=check(red,blue,nums,forRed,forBlue,j,visited,scores)
    
#     perm1=int("".join(forRed))
#     perm2=int("".join(forBlue))
    
#     if len(str(perm1))==nums and len(str(perm2))==nums:
#         # print("here: ",perm1," ",perm2)
#         if perm1>perm2:
#             scores[0]+=1
#         elif perm1<perm2:
#             scores[1]+=1
#         else:
#             scores[2]+=1

#     visited.remove(i)
#     forRed.pop()
#     forBlue.pop()

#     return scores

# def permituate(nums,red,blue):
#     if red==blue:
#         print("EQUAL")
#     else:
#         forRed=[]
#         forBlue=[]
#         scores=[0,0,0]
#         for i in range(nums):
#             visited=set()
#             forRed.append(red[i])
#             forBlue.append(blue[i])
#             visited.add(i)
#             scores=check(red,blue,nums,forRed,forBlue,i,visited,scores)
#         # print("scores: ",scores)
#         maxi=0
#         index=-1
#         for i in range(len(scores)):
#             if scores[i]>maxi:
#                 maxi=scores[i]
#                 index=i

#         if index==0:
#             print("RED")
#         elif index==1:
#             print("BLUE")
#         else:
#             print("EQUAL")

def permituate(nums,red,blue):
    forRed=forBlue=0
    for i in range(nums):
        if int(red[i])>int(blue[i]):
            forRed+=1
        elif int(red[i])<int(blue[i]):
            forBlue+=1
            
    if forRed>forBlue:
        print("RED")
    elif forBlue>forRed:
        print("BLUE")
    else:
        print("EQUAL")

n=eval(input())
lengths=[]
reds=[]
blues=[]
for i in range(n):
    nums=eval(input())
    red=input()
    blue=input()
    lengths.append(nums)
    reds.append(red)
    blues.append(blue)

for i in range(len(lengths)):
    permituate(lengths[i],reds[i],blues[i])
