n=int(input("Enter a number: "))
x=0  
while n>0:
    y=n%10
    x+=y
    n=n//10
print(x,"is sum of digit")
