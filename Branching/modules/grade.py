def average(a,b,c):
    total=a+b+c
    marks=total/3
    print("Average:",marks)
    if marks>=90:
        print("grade:A+")
    elif marks>=75:
        print("grade:A")
    elif marks>=60:
        print("grade:B")
    elif marks>=45:
        print("grade:c")
    else:
        return"Fail"
    