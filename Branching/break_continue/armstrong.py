n=input("enter a number: ")
l=len(n)
print("length is",l)
n=int(n)
z=n
sum=0
while n>0:
    number=n%10
    sum +=number**3
    n//=10
if sum==z:
    print(n,"is an armstrong number")
else:
    print(n,"is not an amstrong number")