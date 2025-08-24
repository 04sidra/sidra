a=[]
n=int(input("enter the limit:"))
for i in range(n):
    e=int(input("enter the elements: "))
    a.append(e)    
print("list=",a)
b=[]
m=int(input("enter the limit:"))
for i in range(m):
    e=int(input("enter the elements: "))
    b.append(e)    
print("list=",b)
for i in a:
    if i%2==0:
        b.append(i)
        a.remove(i)
for i in b:
    if i%2!=0:
        a.append(i)
        b.remove(i)
print("odd number=",a)
print("even numbers=",b)