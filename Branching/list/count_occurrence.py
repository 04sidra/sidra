a=[]
n=int(input("enter the limit: "))
for i in range(n):
    c=int(input("enter the element: "))
    a.append(c)
count={}
for i in a:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

print("list:",a)
print("elements count: ",count)   