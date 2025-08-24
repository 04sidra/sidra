a=[]
n=int(input("enter a limit: "))
for i in range(n):
    c=int(input("enter the elements: "))
    a.append(c)
minmum=a[0]
for j in a:
    if j<minmum:
        minmum=j
print("list of elements",a)
print("minimum value is:",minmum)            