n=input("enter a word: ")
a=""
for i in n:
    if i not in a:
     c=n.count(i)
     print(f"the word {n}  is  {c}  of  {i}")
     a+=i