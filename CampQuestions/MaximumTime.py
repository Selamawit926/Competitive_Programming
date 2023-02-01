def change(inp):
    lst=[]
    for i in range(len(inp)):
        if inp[i]=="?":
            if i==0:
                lst.append("2")
            elif i==1:
                if lst[i-1]=="1":
                    lst.append("9")
                else:
                    lst.append("3")
            elif i==3:
                lst.append("5")
            else:
                lst.append("9")
        else:
            lst.append(inp[i])
    time="".join(lst)
    return time

print(change("?4:5?"))