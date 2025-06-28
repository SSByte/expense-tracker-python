import os

class Expense:
    def __init__(self, amount, category, note):
        self.amount = amount
        self.category = category
        self.note = note

    def __str__(self):
        return f"₹{self.amount} | {self.category} - {self.note}"


class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.load_expenses()

    def add_expense(self, amount, category, note):
        expense = Expense(amount, category, note)
        self.expenses.append(expense)
        print("✅ Expense added!")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses yet.")
        else:
            print("\n📋 Your Expenses:")
            for i, exp in enumerate(self.expenses, 1):
                print(f"{i}. {exp}")

    def total_expenses(self):
        total = sum(exp.amount for exp in self.expenses)
        print(f"\n💰 Total Spent: ₹{total}")

    def save_expenses(self):
        with open("expenses.txt", "w") as file:
            for exp in self.expenses:
                file.write(f"{exp.amount},{exp.category},{exp.note}\n")

    def load_expenses(self):
        if os.path.exists("expenses.txt"):
            with open("expenses.txt", "r") as file:
                for line in file:
                    parts = line.strip().split(',')
                    if len(parts) == 3:
                        amount = float(parts[0])
                        category = parts[1]
                        note = parts[2]
                        self.expenses.append(Expense(amount, category, note))


def main():
    tracker = ExpenseTracker()

    while True:
        print("\n💸 Expense Tracker Menu")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            try:
                amount = float(input("Enter amount (₹): "))
                category = input("Enter category (e.g. Food, Travel): ")
                note = input("Add a note: ")
                tracker.add_expense(amount, category, note)
            except ValueError:
                print("❌ Invalid amount. Please enter a number.")
        elif choice == '2':
            tracker.view_expenses()
        elif choice == '3':
            tracker.total_expenses()
        elif choice == '4':
            tracker.save_expenses()
            print("💾 Saved and exited. See you!")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
