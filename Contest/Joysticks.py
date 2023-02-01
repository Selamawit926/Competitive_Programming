line=input().split(" ")
joy1=int(line[0])
joy2=int(line[1])
first=second=0
if joy1==1 and joy2==1:
    print(0)
else:
    if joy1>joy2:
        first=joy2
        second=joy1
    else:
        first=joy1
        second=joy2

    count=0
    while first>0 and second>0:
        if second>2:
            first+=1
            second-=2
            count+=1

        else:
            if first<=2:
                count+=1
                break

            temp=first
            first=second
            second=temp

    print(count)