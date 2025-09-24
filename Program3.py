def check(x):
    if x%2==0:
        x=x-1
    num=1
    for i in range(x):
        print(num,end=" ")
        num=num+2
    
x=int(input("Enter the Integer : "))
check(x)
