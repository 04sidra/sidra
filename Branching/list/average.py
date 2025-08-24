a=[]
n=int(input("enter a limit: "))
for i in range(n):
    c=int(input("enter the elements: "))
    a.append(c)
average=sum(a)/len(a)
print("lists: ",a)
print("average is: ",average)
