n=eval(input())
ans=[]
for i in range(n):
    first=input().split(" ")
    second=input().split(" ")
    x1=first[0]
    p1=first[1]
    x2=second[0]
    p2=second[1]
    # print(len(x1)+int(p1))
    # print(len(x2)+int(p2))
    if len(x1)+int(p1)>len(x2)+int(p2):
        ans.append(">")
    elif len(x1)+int(p1)<len(x2)+int(p2):
        ans.append("<")
    else:
        if x1==x2 and p1==p2:
            ans.append("=")
        else:
            pos={1,10,100,1000,10000,100000,1000000}
            if int(x1)>int(x2) and int(x1)%int(x2)==0 and int(x1)//int(x2) in pos:
                if int(p2)-int(p1)==len(x1)-len(x2):
                    ans.append("=")
                elif int(p2)-int(p1)>len(x1)-len(x2):
                    ans.append("<")
                else:
                    ans.append(">")
            elif int(x2)>=int(x1) and int(x2)%int(x1)==0 and int(x2)//int(x1) in pos:
                if int(p1)-int(p2)==len(x2)-len(x1):
                    ans.append("=")
                elif int(p1)-int(p2)>len(x2)-len(x1):
                    ans.append(">")
                else:
                    ans.append("<")

            else:
                if int(x1[0])>int(x2[0]):
                    ans.append(">")
                elif int(x1[0])<int(x2[0]):
                    ans.append("<")
                else:
                    if int(x1)>int(x2):
                        ans.append(">")
                    elif int(x1)<int(x2):
                        ans.append("<")
                    else:
                        ans.append("=")
          
for i in ans:
    print(i)
