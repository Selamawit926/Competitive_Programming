import math
n=eval(input())
def prime(n):
    if n==2:
        print(-1)
    else:
        odd=n-2
        found=False
        sqrt=math.sqrt(odd)
        if sqrt!=math.floor(sqrt):
            sqrt=math.floor(sqrt)
            for i in range(2,sqrt):
                if odd%i==0:
                    found=True
                    print(-1)
                    break
            if not found:
                print("2 "+str(odd))

        else:
            print(-1)
prime(n)
