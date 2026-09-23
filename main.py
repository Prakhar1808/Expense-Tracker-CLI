from storage import add_expenses, show_expenses
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("command", choices = ["add", "show"], help = "what to do")
parser.add_argument('-c', '--category', help = "Category of expenditre")
parser.add_argument('-a', '--amount', type = float, help = "Amount spent")
parser.add_argument('-li', '--listcat', default = "all", help = "category specific expenditure to list")
args = parser.parse_args()

if args.command == "add":
    add_expenses(args.category, args.amount)

else:
    show_expenses(args.listcat)

print("Exiting Safely")
