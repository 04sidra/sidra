a=[]
n=int(input("Enter the number of elements: "))
for i in range(n):
    b=int(input("Enter element: "))
    a.append(b)
for i in a:
    if i<2:
        print(i,"is not a prime number")
    else:
        prime = True
        for j in range(2,i):
            if i%j==0:
                prime=False
                break
        if prime:
            print(i,"is a prime number")
        else:
            print(i,"is not a prime number")
