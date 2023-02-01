import sys

sys.stdin=open("trial2.txt")
files= sys.stdin.readlines()

def reader(files):
    word=files[0]
    di={}
    for i in word:
        if i in di:
            di[i]+=1
        else:
            di[i]=1
    maxi=1
    maxi=max(maxi,di.values())
    if maxi>1:
        if maxi%2==0:
            print(2)
        

