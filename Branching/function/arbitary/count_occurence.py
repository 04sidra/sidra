def count_occurence(*n):
    count={}
    for i in n:
        if i in count:
           count[i] += 1
        else:
            count[i] = 1
    return count
print(count_occurence(2,2,2,3,4,5,6,5))        