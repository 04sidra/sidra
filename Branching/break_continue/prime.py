n=int(input("enter a number: "))
i=2
while i<n:
    if n%i==0:
        print(n,"is not prime number")
        break
        i+=1
    else:
         print(n,"is prime number")  
         break