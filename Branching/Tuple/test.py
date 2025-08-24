#first largest
a = []
n = int(input("enter the limit :"))
for i in range(n):
        b = int(input("enter the number :"))
        a.append(b)
print("list :",a)        
largest=0
for j in a:
    if j>largest:
       largest=j
print("largest number is :",largest)       
 
