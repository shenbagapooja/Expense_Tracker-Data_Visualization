import json
import pandas as pd
import matplotlib.pyplot as plt

with open("Expenses.json", "r") as file:
    expenses = json.load(file)

while True:
   
 print("===== EXPENSE TRACKER =====")
 print("1. Add Expense")
 print("2. View Expenses")
 print("3. Delete Expense")
 print("4. Expenses analysis")
 print("5. Exit")

 choice = input("Enter your choice: ")

 if choice == "1":
   print("Adding expenses")
   name = input("Enter the expense name:")

   try:
    amount = float(input("Enter the expense amount: "))
   except ValueError:
     print("Please enter a valid amount!")
     continue

   category = input("Enter the category of the expense:").lower()
   date = input("Enter the expense date:")
 
   expense = {
    "name": name,
    "amount": amount,
    "category": category,
    "date": date
   }
   expenses.append(expense)

   with open("Expenses.json", "w") as file:
    json.dump(expenses, file, indent=4)

 elif choice == "2":
    print("Viewing expenses")

    for expense in expenses:
        print("Name:", expense["name"])
        print("Amount:", expense["amount"])
        print("Category:", expense["category"])
        print("Date:", expense["date"])
        print()

 elif choice == "3":
   try:
    number = int(input("Enter the expense number to delete: "))

    if number < 1 or number > len(expenses):
        print("Invalid expense number!")
        continue

    del expenses[number - 1]

   except ValueError:
     print("Please enter a valid number!")
     continue

   with open("Expenses.json", "w") as file:
      json.dump(expenses, file, indent=4)

 elif choice == "4":
    df = pd.DataFrame(expenses)

    category_expense = df.groupby("category")["amount"].sum()

    print("===== EXPENSE ANALYSIS =====")
    print("1. Bar Chart")
    print("2. Pie Chart")
    print("3. Summary")
    print("4. Back")

    analysis_choice = input("Enter your choice: ")
    if analysis_choice == "1":
       plt.bar(category_expense.index, category_expense.values)

       plt.xlabel("Category")
       plt.ylabel("Amount")
       plt.title("Expenses by Category")

       plt.show()

    elif analysis_choice == "2":
      plt.pie(category_expense.values, labels=category_expense.index, autopct="%1.1f%%")

      plt.title("Expenses by Category")

      plt.show()

    elif analysis_choice == "3":
     print("===== EXPENSE SUMMARY =====")

     print("Total Expense:", df["amount"].sum())
     print("Highest Expense:", df["amount"].max())
     print("Lowest Expense:", df["amount"].min())
     print("Average Expense:", df["amount"].mean())

     print("Category-wise Expenses:")
 
     for category, amount in category_expense.items():
         print(category, ":", amount)
         
    elif analysis_choice == "4":
     continue
      
    else:
      print("Invalid choice!")

 elif choice == "5":
    print("Have a nice day !")
    break
 else:
    print("Invalid!")  
   
