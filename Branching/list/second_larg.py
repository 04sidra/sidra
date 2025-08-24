a=[]
n=int(input("enter the number: "))
for i in range(n):
    b=int(input("enter the elements: "))
    a.append(b)
big=a[0]
for i in range(1,n):
    if a[i]>big:
        big=a[i]
i=0
while(1):
    if a[i]!=big:
        sbig=a[i]
        break
    i+=1
for i in range(i+1,n):
    if a[i]<big and a[i]>sbig:
        sbig=a[i] 
print("Biggest elements: ",big)
print("second biggest",sbig)                       