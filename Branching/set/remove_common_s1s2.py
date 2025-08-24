s1={1,2,3,4,5,6,7,8}
s2={5,6,7,8,9,10,11}
for i in list(s1):
    if i in s2:
        s1.remove(i)
print(s1)        