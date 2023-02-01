def calculate(n,count):
    lst=[1]*len(n)
    lst2=[1]*len(n)+1
    lower="".join(lst)
    upper="".join(lst2)
    count+=len(lower)
    
    count=calculate(lower,count)
    count=calculate(upper,count)

n=eval(input)
count=0
lst=[1]*len(n)
lst2=[1]*len(n)+1
lower="".join(lst)
upper="".join(lst2)
count=calculate(lower,count)
count=calculate(upper,count)


    

