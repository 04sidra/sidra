n=int(input("enter a limit: "))
a=[]
for i in range(n):
    c=int(input("enter the number"))
    a.append(c)
print("list",a)    
for j in a:
    if j%2==0:
       print("number is even",c)
    j+=1
else:
    print("number is not even",c)           
    