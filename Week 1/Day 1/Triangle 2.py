
def xmasTree(a):
    m= "* "
    n=" "
    c=a
    for i in range(1,a+1):
        if i==1:
            print(n*c + m +'\n')
            c-=1
        else:
            print(n*c+ m*i + '\n')
            c-=1

a=eval(input("Enter number: "))
xmasTree(a)


