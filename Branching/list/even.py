a=[]
n=int(input("enter a limit: "))
for i in range(n):
    c=int(input("enter the elements: "))
    a.append(c)
print("even number is:")
for j in a:
    if j%2==0:
        print(j)