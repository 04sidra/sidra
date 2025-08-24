def max_min(*n):
    max= n[0]
    min= n[0]
    for i in n:
        if i > max:
            max= i
        if i < min:
            min= i
    return max,min
mx, mn =max_min(10, 25, 3, 89, 2, 77)
print("Maximum:", mx)
print("Minimum:", mn)
