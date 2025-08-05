n=str(input("enter a word : "))
vowels="aeiouAEIOU"
count=0
for i in n:
    for j in vowels:
     if i==j:
        count+=1
print(count)