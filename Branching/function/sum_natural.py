def sum_natural(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
    return sum    
n1=int(input("enter the number : "))    
print("sum of natural numbers is ",sum_natural(n1))    

