n=int(input("enter a number: "))
sum=0  
while n>0:
    y=n%10
    sum+=y
    n=n//10
print(sum,"is sum of digit")
