
def formTeam(lst):
    lst.sort()
    maxi=0
    count=0
    left=0
    right=0
    iteration=0
    while right<len(lst):
        iteration+=1
        # print(left,right)
        if (lst[right]-lst[left]<=5):
            count+=1
        else:
            left+=1
            # print(left,right)
            count=(right-left)+1

        maxi=max(maxi,count)
        right+=1
            
    maxi=max(maxi,count)
    # print(iteration)
    print(maxi)

def reader():
    n = int(input())
    nums = input().split(' ')
    lst=[]
    for i in nums:
        lst.append(int(i))
    formTeam(lst)
reader()
