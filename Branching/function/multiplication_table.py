def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")
n1=int(input("Enter a number: "))
print(multiplication_table(n1))
