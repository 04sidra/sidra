def fact_num(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact    
n1=int(input("enter the number  :"))
print(fact_num(n1))
