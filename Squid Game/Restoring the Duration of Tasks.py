cases=input()
tests=cases.split()
output=[]
for i in range(int(tests[0])):
    n=input()
    ans=[]
    inp=input()
    nums=inp.split(" ")
    t=input()
    time=t.split(" ")
    prev=int(time[0])
    ans.append(int(time[0])-int(nums[0]))
    for j in range(1,len(nums)):
        if int(nums[j])<prev:
            ans.append(int(time[j])-prev)
        else:
            # print(int(time[j]),int(nums[j]))
            ans.append(int(time[j])-int(nums[j]))
        prev=int(time[j])
    output.append(ans)
for i in output:
    for j in i:
        print(j,end=" ")
    print()