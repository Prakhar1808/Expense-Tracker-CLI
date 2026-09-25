## Expense Tracker!

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![Argparse](https://img.shields.io/badge/stdlib-argparse-red)

track your expenses easily
> i built this project because i can't track my expenses

### Introduction
this project was built to learn about CLI using argparser
some features i implemented along the project:
- [x] Error Messages
- [x] Parser Arguments (duh)
- [x] Default input type flag
- [ ] using optional flag
- [x] Help messages
- [x] Use of csv to save expenses

### Navigation
the very basic structure:
```
Expense-Tracker/
├── main.py
├── storage.py
├── README.md (you're here, hi!)
└── expenses.csv (persistent storage)
```

### Usage
+ arguments used:
```bash
command          add | show        (choices, positional)
-c/--category    expense category
-a/--amount      amount spent  (must be a number)
-li/--listcat    category to list, default "all"
```

some examples to run and play around with
```bash
python3 main.py --help
python3 main.py add --category biryani --amount 60.0
python3 main.py add --category travel --amount 137.8
python3 main.py show
python3 main.py show --listcat food
```
to clone and locally run the project:
```bash
git clone https://github.com/Prakhar1808/Expense-Tracker.git
```

### Behaviour
+ negative expense is supported but 0 is not
+ error when using "add" but no valid category or amount given

### Requirements
Python 3, zero third-party dependencies (argparse + csv are stdlib), so no venv
