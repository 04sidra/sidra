a={1,2,3,4,5}
b={3,4,5,6,7}
for i in list(a):
    if i  in b:
       a.remove(i)
print(a)