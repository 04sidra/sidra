n=input("Enter a Word : ")
for i in range(len(n)):
    temp=0
    for j in range(len(n)): 
        if n[i]==n[j] and i!=j:
            temp+=1
if temp:
    print("The characters are not unique")
else:
    print("The characters are unique")