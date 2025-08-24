a=[]
n=int(input("enter the limit: "))
for i in range(n):
    c=int(input("enter the element: "))
    a.append(c)
b=[]
for i in a:
    if i not in b:
        b.append(i)

print("list:",a)
print("list removing duplications: ",b)    