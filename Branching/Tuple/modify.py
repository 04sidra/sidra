a=(10,20,30,40)
print("original tuple:",a)
temp=list(a)
for i in range(len(temp)):
    if temp[i]==20:
        temp[i]=25
a=tuple(temp)
print("Modified tuple:",a)
