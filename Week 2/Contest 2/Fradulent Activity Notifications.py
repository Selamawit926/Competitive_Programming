def activityNotifications(expenditure, d):
    count=0
    f=d
    for i in range(0,len(expenditure)-d):

        lst=expenditure[i:f]
        lst3=[0]*(max(lst)+1)
        lst2=[]

        for i in lst:
            lst3[i]+=1
            

        for i in range(0,len(lst3)):
            for k in range(0,lst3[i]):
                lst2.append(i)

        if len(lst2)%2==0:
            size=len(lst2)//2
            med=(lst2[size]+lst2[size-1])/2

        else:
            size=(len(lst2)+1)//2
            med=lst2[size-1]

        if expenditure[d]>=med*2:
            count+=1
        
        f=f+1
    print(count)


activityNotifications([1,2,3,4,4],4)
