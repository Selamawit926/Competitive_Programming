
ranked=[100,90,90,80,75,60]
player=[50,65,77,90,102]
lst=[ranked[0]]
lst2=[0]*len(ranked)
for i in range(1,len(ranked)):
    if ranked[i]!=lst[i-1]:
        lst.append(ranked[i])
        lst2[i]=lst2[i-1]+1
    elif ranked[i]==lst[i-1]:
        lst2[i]=i-1
        

print(lst2)


# for i in range(1,len(ranked)):
#     if ranked[i]==ranked[i-1]:
#         lst[i]=i-1
#         # print(lst)
#     elif i-lst[i-1]>1:
#         lst[i]=lst[i-1]+1
#         # print(lst)
#     else:
#         lst[i]=i
#         # print(lst)

# print(lst)
           




# lst=[0]*len(player)
# for i in range(0,len(player)):
#     for j in range(0,len(ranked)):
#         if player[i]<ranked[len(ranked)-1]:
#             lst[i]=len(ranked)
#             ranked.append(player[i])
#             break
        
#         elif player[i]>ranked[j]:
#             lst[i]= j
#             break
#         elif player[i]==ranked[j]:

#     print(lst)
