a=[]
n=int(input("enter the limit: "))
for i in range(n):
    c=int(input("enter the elements: "))
    a.append(c)
b=int(input("check the list:"))
if b in a:
    print(b,"exists in the list")
else:
    print(b," does not exist in the list")
print("list",a)        

