n=input("enter a word: ")
a=input('enter a letter to check: ')
count=0
for i in n:
    if i==a:
     count+=1
print(f"in {n} have {count},{a}")