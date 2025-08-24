# shope={'skirt':800,'Top':500,'inner wear':350,'saree':1500,'lahangha':4000}
# cart={}
# print("   SIDRA WEDDING MALL   ")
# exit =1
# while exit:
#     print("1.Available items and price\n2.Add items to the cart along with their quantities\n3.View the cart and the total bill amount\n4.Chekout and display the final bill")
#     want=int(input("enter the option : "))
#     if want==1:
#         print(shope)
#     elif want==2:
#         print(shope)
#         item = input("Choose Item : ")
#         quantity = int(input("Enter quantity : "))
#         if item in shope:
#             cart.update({'item':quantity})
#         else:
#             print("enter invalid item")
#     elif want==3:        
#         if cart:
#             print("\n your cart:")  
#             total=0
#             for item,quantity in cart.item():
#                 price=shope[item]*quantity  
#                 total+=price
#                 print(f"{item} x {quantity}=${price}")
#             print(f"Total:${total}")
#         else:
#             print("Your cart is empty.")
#     elif want==4:
#         if cart:
#             print("\n Bill ")
#             total=0
#             for item,quantity in cart.item():
#                 price=shope[item]*quantity
#                 total+=price
#                 print(f"{item} x {quantity}=${price}")
#             print(f"Final Total:${total}")
#             print("Thank you for shopping") 
#             cart.clear()
#         else:
#             print("Your cart is")       
shope = {
    'skirt': 800,
    'Top': 500,
    'inner wear': 350,
    'saree': 1500,
    'lahangha': 4000
}
cart={}
print("   SIDRA WEDDING MALL   ")
sale=True
while sale:
    print("\n1. Available items and price")
    print("2. Add items to the cart along with their quantities")
    print("3. View the cart and the total bill amount")
    print("4. Checkout and display the final bill")
    print("5. Exit")
    want=int(input("Enter the option: "))
    if want==1:
        print("\nAvailable Items:")
        for item, price in shope.items():
            print(f"{item}:₹{price}")

    elif want==2:
        print("\nAvailable Items:")
        for item, price in shope.items():
            print(f"{item}:₹{price}")
        item=input("Choose Item: ")
        quantity=int(input("Enter quantity: "))
        if item in shope:
            if item in cart:
                cart[item]+=quantity
            else:
                cart[item]=quantity
            print(f"{quantity}{item}(s)added to cart.")
        else:
            print("Invalid item entered.")
    elif want==3:
        if cart:
            print("\nYour Cart:")
            total=0
            for item,quantity in cart.items():
                price=shope[item]*quantity
                total+=price
                print(f"{item}x{quantity}=₹{price}")
            print(f"Total: ₹{total}")
        else:
            print("Your cart is empty.")

    elif want==4:
        if cart:
            print("\nFinal Bill")
            total=0
            for item, quantity in cart.items():
                price=shope[item]*quantity
                total+=price
                print(f"{item}x{quantity}=₹{price}")
            print(f"Final Total:₹{total}")
            print("Thank you for shopping with SIDRA WEDDING MALL!")
            cart.clear()
        else:
            print("Your cart is empty.")

    elif want==5:
        sale=False
        print("Exiting... Thank you for visiting!")

    else:
        print("Invalid option. Please try again.")




      

        