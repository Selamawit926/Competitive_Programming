
# recursive
def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        x=n*factorial(n-1)
        return x

print(factorial(5))

# iterative
x=1
n=5
if n==0:
    print(1)

for i in range(n,0,-1):
    x=x*i

print(x)