n=int(input("enter a number: "))
sum=0
while n>0:
    y=n%10
    sum+=y
    n=n//10
    if n==0 and sum>9:
        n=sum
        sum=0 
print(sum)      