def multiplication_all_number(*n):
    for num in n:  
        print(f"\nMultiplication Table of {num}:")
        for i in range(1, 11):
            print(f"{num} x {i} = {num * i}")
print(multiplication_all_number(10,5,9))