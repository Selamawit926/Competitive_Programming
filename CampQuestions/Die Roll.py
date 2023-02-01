points=input().split(" ")
yakko=int(points[0])
wakko=int(points[1])
maxi=max(yakko,wakko)
numerator=(6-maxi)+1
denominator=6
i=2
newNumerator=numerator
newDenominator=denominator
while i<=numerator:
    if newNumerator%i==0 and newDenominator%i==0:
        newNumerator=newNumerator//i
        newDenominator=newDenominator//i
    i+=1

print(str(newNumerator)+"/"+str(newDenominator))