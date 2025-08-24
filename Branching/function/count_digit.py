def count_digit_num(n):
    count = 0
    while n > 0:
        count += 1
        n //= 10   
    return count
n1=int(input("Enter a number: "))
print("Number of digits is", count_digit_num(n1))
