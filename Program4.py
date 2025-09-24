def check(nums):
    dict={i:0 for i in range(1,10)}
    for num in nums:
        for i in range(1,10):
            if(num%i==0):
                dict[i]=dict[i]+1
    print(dict)
    
a=list(map(int,input("Enter the list of numbers : ").split()))
check(a)
