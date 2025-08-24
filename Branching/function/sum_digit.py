def sum_of_digit(n):
    sum=0  
    while n>0:
        y=n%10
        sum+=y
        n=n//10
    return sum
n1=int(input("enter the number : ")) 
print(sum_of_digit(n1))   