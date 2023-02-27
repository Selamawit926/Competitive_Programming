cases=input()
testcases=cases.split()
output=[]
for i in range(int(testcases[0])):
    n=input()
    inp=input()
    nums=inp.split(" ")
    odds=0
    evens=0
    for j in range(len(nums)):
        if int(nums[j])%2==0 and j%2!=0:
            evens+=1
        if int(nums[j])%2!=0 and j%2==0:
            odds+=1
    if evens==odds:
        output.append(evens)
    else:
        output.append(-1)
for i in output:
    print(i)