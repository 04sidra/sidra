a={1,2,3,4}
b={3,4,5,6}
common=set()
for i in a:
    if i in b:
        common.add(i)
print(common) 
