a=[]
n=int(input("Enter the number of elements: "))
for i in range(n):
    c=int(input("Enter element: "))
    a.append(c)
sum=0
for i in a:
    if i%2==0:
        sum+=i
print("List:", a)
print("Sum of even numbers:",sum)
