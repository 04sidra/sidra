a=(50,10,30,20,40)
print("Original tuple:",a)
temp=list(a)
for i in range(len(temp)):
    for j in range(i+1,len(temp)):
        if temp[i]>temp[j]:
            temp[i],temp[j]=temp[j],temp[i]
sorted=tuple(temp)
print("Sorted:",sorted)
