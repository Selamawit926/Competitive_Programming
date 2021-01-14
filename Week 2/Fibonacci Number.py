#recursive

def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)

print(fib(7))
# iterative
f0=1
f1=1
n=7
for i in range(0,n-2):
    f=f0+f1
    f0=f1
    f1=f

print(f)

    