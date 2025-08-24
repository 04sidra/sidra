a={1,2,3,4,5,6}
b={4,5,6,7,8,9}
for i in a:
    if i in b:
        common=a.intersection(b)
        print(common)
        break
else:
     print('No Common')
