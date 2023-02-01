n=input().split(" ")
# ans=max(4,(int(n[0])*int(n[1]))**2)
ans=2**(int(n[0])+int(n[1]))%(998244353) 
print(ans)