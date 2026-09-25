from storage import add_expenses, show_expenses
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("command", choices = ["add", "show"], help = "choices to choose from")
parser.add_argument('-c', '--category', help = "expenditure category")
parser.add_argument('-a', '--amount', type = float, help = "Amount spent")
parser.add_argument('-li', '--listcat', default = "all", help = "category specific expenditure to list")
args = parser.parse_args()

if args.command == "add":
    if not args.category or not args.amount:
        parser.error("\"add\" requires both --category and --amount both to be valid")
    add_expenses(args.category, args.amount)

else:
    show_expenses(args.listcat)
