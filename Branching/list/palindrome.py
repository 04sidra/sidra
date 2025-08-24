a=[]
n=int(input("enter a limit: "))
for i in range(n):
    c=int(input("enter a element: "))
    a.append(c)
palindrome=True    
for i in range(len(a) // 2):
    if a[i] != a[-(i + 1)]:
         palindrome=False
         break
print("List:",a)
if palindrome:    
         print("the list is palindrome")
else:
         print("the list is not a palimdrome")          