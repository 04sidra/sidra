a=[]
n=int(input("enter the number: "))
for i in range(n):
    b=int(input("enter the elements: "))
    a.append(b)
#print("lists",a)
list=tuple(a)
print("Tuple:",list)
#if len(list)>=5:
num=list[4]
    #print("The 5th item is:",num)
if num==20:
        print("the 5th item is 20")
else:
        print("The 5th item is not 20.")