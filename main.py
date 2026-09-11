expenses = []
#TODO: store the expenses in a csv file

while True: # The loop which takes input and decides the choices
    choice = input("Enter Your Choice (add, list or quit): ").lower()

    if choice == "add":
        amount = input("How much is the Amount? ")
        category = input("What category of expense? ").lower()
        expenses.append([category, amount])

    elif choice == "list":
        user_input = input("which Category to display or \"all\": ")
        if user_input == "all":
            print(expenses)
        else:
            for i in range(len(expenses)):
                if user_input == expenses[i][0]:
                    print(expenses[i][1])

    elif choice == "quit":
        break
print("Exiting Safely")
