def reverse_num(n):
    rev = 0
    while n > 0:
        digit = n % 10      
        rev = rev * 10 + digit
        n //= 10           
    return rev
n1=int(input("Enter a number: "))
print("Reversed number is", reverse_num(n1))
