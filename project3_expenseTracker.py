import csv
from datetime import datetime

def add_expense():
    #Add an expense to the expense tracker.
    #The user will be prompted to enter the expense name, amount, and date.
    date = input("Enter the date (YYYY-MM-DD): ")
    amount = float(input("Enter the amount: "))
    description = input("Enter a description: ")
    category = input("Enter the category: ")

    with open("expenses.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([date, amount, description, category])

def view_expenses():
    #View all expenses in the expense tracker.
    print("Date\t\tAmount\t\tDescription\tCategory")
    print("-------------------------------------------------------------")

    with open("expenses.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print("\t\t".join(row))

def view_summary():
    #View a summary of monthly expenses.
    month_data = {}

    with open("expenses.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)  # Skip header row
        for row in reader:
            #reading date
            date = datetime.strptime(row[0], "%Y-%m-%d")
            amount = float(row[1])
            month = date.strftime("%Y-%m")
            #expenses teacker by months by taking total amount and category of expenses and amount
            if month not in month_data:
                month_data[month] = {"total": 0, "categories": {}}
            #month wise expenses
            month_data[month]["total"] += amount
            #category wise expenses
            category = row[3]
            if category not in month_data[month]["categories"]:
                month_data[month]["categories"][category] = 0
            month_data[month]["categories"][category] += amount
    #printingf the summary of expenses by monthly
    print("Monthly Summary")
    print("-------------------")
    for month, data in month_data.items():
        print(f"{month}: {data['total']:.2f}")
        for category, amount in data["categories"].items():
            print(f"\t{category}: {amount:.2f}")
        print()

def main():
    #Main function to run the expense tracker Application.
    print("Welcome to the Expense Tracker!")
    print("--------------------------------")
    #giving options to the user for the user tasks on the applications.
    #option:1-->add expenses
    #option:2-->view expenses
    #option:3-->summary of expenses by monthly
    while True:
        print("\nOptions:")
        print("1. Add an expense")
        print("2. View expenses")
        print("3. View summary")
        print("4. Quit")

        option = int(input("Enter your option: "))

        if option == 1:
            add_expense()
        elif option == 2:
            view_expenses()
        elif option == 3:
            view_summary()
        elif option == 4:
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
