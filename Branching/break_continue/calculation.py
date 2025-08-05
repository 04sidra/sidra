a=int(input("enter a number: "))
b=int(input("enter a number: "))
print('''
      1.Addition
      2.Substraction
      3.Division
      4.Multiplication''')
option=int(input("enter a choice: "))
while option<=4:
    if option==1:
        sum=a+b
        print(sum)
        break
    elif option==2:
        sub=a-b
        print(sub)
        break
    elif option==3:
        div=a/b
        print(sum)
        break
    elif option==4:
        mul=a*b
        print(mul)
        break            