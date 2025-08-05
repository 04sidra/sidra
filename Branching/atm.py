balance=int(input("enter the balance:"))
withdraw=int(input("enter the amount:"))
if balance<withdraw:
    print("insufficient bank balance")
elif withdraw%100!=0:
     print("invalid")
else:
     print("withdraw successfull balance amount",balance-withdraw)
