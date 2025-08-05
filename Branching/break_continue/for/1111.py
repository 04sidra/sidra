n=int(input("enter a number: "))
a=1
for i in range(1,n+2):
    n-=1
    for j in range(1,n+2):
        print(j,end=" ")
        a+=1
    print()   