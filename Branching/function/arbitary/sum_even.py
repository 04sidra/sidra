def sum_even(*n):
    s=0
    for i in n:
        if i % 2 == 0:  
            s+=i
    return s   
print(sum_even(1, 2, 3, 4, 5, 6))   

