a=[]
n=int(input("enter the number: "))
for i in range(n):
    b=int(input("enter the elements: "))
    a.append(b)
print("lists",a)    
rev=()
for i in range(len(a)- 1, -1, -1):
    rev+=(a[i],)

print("Original Tuple:",a)
print("Reversed Tuple:",rev)