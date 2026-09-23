from storage import add_expenses, show_expenses

while True: # The loop which takes input and decides the choices
    choice = input("Enter Your Choice (add, list or quit): ").lower()

    if choice == "add":
        amount = float(input("How much is the Amount? "))
        category = input("What category of expense? ").lower()
        add_expenses(category, amount)

    elif choice == "list":
        user_input = input("which Category to display or \"all\": ").lower()
        show_expenses(user_input)

    elif choice in ["quit", "q"]:
        break
print("Exiting Safely")
