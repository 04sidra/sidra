list1=[1,2,3,4,5,5]
list2=[5,5,6,7,2,1]
c=[]
for i in list1:
    for j in list2:
        if i==j:
            a=False
            print(f"value of i {i} j {j}")
            for k in c:
                if k==i:
                    a=True
                    break
            if not a:
                c.append(i)
print("common elements",c)
                    