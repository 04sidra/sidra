list1 = [2,23,1,7,23,789,7]
removedup = [list1[i] for i in range(len(list1)) for j in range(len(list1)) if list1[i] == list1[j] and i!=j]
print(removedup)