a=[]
n=int(input("enter a limit: "))
for i in range(n):
    c=int(input("enter the elements: "))
    a.append(c)
sum=0
for j in a:
    sum+=j
print("list of elements",a)
print("sum of elements",sum)