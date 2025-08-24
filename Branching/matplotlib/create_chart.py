# import matplotlib.pyplot as plt
# # part of the figure
# slices=[50,20,20,10]
# # labales of the figure
# l=['food','rent','shopping','extra']
# # color
# c=['red','yellow','magenta','blue']
# plt.pie(slices, labels=l, colors=c)
# plt.title('Expenses')
# plt.show()
import csv
import os
import matplotlib.pyplot as plt   # for charts
import pandas as pd               # easier CSV handling

def register_student():
    print("----- Student Registration -----")
    
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    weight = input("Enter your weight: ")
    place = input("Enter your place: ")
    steps = input("Enter steps completed in 45 minutes: ")

    file_exists = os.path.isfile("students.csv")

    # Save data into a CSV file
    with open("students.csv", "a", newline="") as file:
        writer = csv.writer(file)
        
        # Write header only if file is new
        if not file_exists:
            writer.writerow(["Name", "Age", "Weight", "Place", "Steps Completed"])
        
        writer.writerow([name, age, weight, place, steps])

    print("✅ Registration Successful!\n")

# 🔹 New function: Show chart of Steps Completed
def show_chart():
    if not os.path.isfile("students.csv"):
        print("❌ No data available. Please register students first.")
        return
    
    # Read CSV using pandas
    df = pd.read_csv("students.csv")
    
    # Plot Steps Completed vs Name
    plt.bar(df["Name"], df["Steps Completed"])
    plt.xlabel("Student Name")
    plt.ylabel("Steps Completed (in 45 mins)")
    plt.title("Student Fitness Chart")
    plt.xticks(rotation=30)  # rotate names for readability
    plt.show()

def menu():
    while True:
        print("\n===== Student Registration Menu =====")
        print("1. Register Student")
        print("2. Show Chart")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            register_student()
        elif choice == "2":
            show_chart()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.\n")

# Run the menu
menu()
