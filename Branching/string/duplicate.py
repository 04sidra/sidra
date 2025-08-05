a=input("enter a string:")
b=""
for i in a:
    if i not in b:
          b+=i
print("string after removing duplictions",b)        