a=[]
n=int(input("enter a limit: "))
for i in range(n):
    c=int(input("enter a element: "))
    a.append(c)
print("lists",a)

odd=[]
even=[]
for j in a:   
    if j%2==0:
        even.append(j)
    else:
        odd.append(j)
print("number is even",even)
print("the number is odd",odd) 