a=(10, 20, 30, 40, 50, 60)
new=()
for i in a:
    if i>30:
        new+=(i,)
print("original tuple:",a)
print("New tuple:",new)
