s1={1,2,3,4,5}
s2={4,5,6,7,8}
for i in s2:
    if i not in s1:
        s1.symmetric_difference_update(s2)
print(s1)