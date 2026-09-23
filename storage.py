import csv
from pathlib import Path

file_path = Path("expenses.csv")

def add_expenses(category: str, amount: float):
    with open(file_path, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([category, amount])

def show_expenses(user_input="all"):
    if file_path.is_file():
        print("\n['Category', 'Amount']\n----------------------------")

        with open(file_path, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == user_input or user_input == "all":
                    print(row)

    else:
        print("No File Exists to read!")

