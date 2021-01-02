
def reverse(x):
    y=""
    b=str(x)
    lst=[]

        
    for i in range(0,len(b)):
        if b[i] == "-":
              y=y+b[i]

        else:
            lst.append(b[i])

    lst.reverse()

    for i in range(0,len(lst)):
        if len(lst)==1:
            break
        if lst[i] == "0":
            lst[i]=""

        else:
            break

    d = ''.join(lst)

    if int(y+d) >= (-2**31) and int(y+d) <= (2**31):
        return y+d
    else:
        return 0

x=eval(input("Enter number: "))
print(reverse(x))
