def bonAppetit(bill, k, b):
    #will be easier to add all the items first to use only one iteration
    #then subtract the number from total for sake of time complexity
    m=0
    bill[k]=0
    for i in bill:
        m=m+i
    m=m//2
    
    if(m==b):
        print("Bon Appetit")
    else:
        print(b-m)

inp=input("Enter list of prices: ")
bill=[eval(inp) for inp in inp.split()]
k=eval(input("Enter the index she didn't eat: "))
b=eval(input("Enter the amount she should pay: "))
bonAppetit(bill,k,b)