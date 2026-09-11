import csv
from pathlib import Path

file_path = Path("expenses.csv")

while True: # The loop which takes input and decides the choices
    choice = input("Enter Your Choice (add, list or quit): ").lower()

    if choice == "add":
        amount = input("How much is the Amount? ")
        category = input("What category of expense? ").lower()

        with open(file_path, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([category, amount])

    elif choice == "list":
        user_input = input("which Category to display or \"all\": ").lower()

        if file_path.is_file():
            print("\n['Category', 'Amount']\n----------------------------")

            with open(file_path, "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == user_input or user_input == "all":
                        print(row)

        else:
            print("No File Exists to read!")

    elif choice == "quit":
        break
print("Exiting Safely")
