from utils import add_note,list_all,mark_done,remove_note
import argparse
'''---------------------------------------------------------------------------------------------------the first code doesnt have argument
choice =""

while choice !="q":
    choice = input("Choose:(ADD) Task, (Remove) Task , (Mark) Done , (List) All ").strip().lower()

    if choice == "add":
        add_note()

    elif choice == "remove":
        remove_note()

    elif choice == "mark":
        mark_done()

    elif choice == "list":
        list_all()

    else:
        print("Invalid choice.")'''
#---------------------------------------------------------------------------------------second code it didnt work
'''parser = argparse.ArgumentParser()
parser.add_argument("--choose",help="Choose( add, remove, list, mark, Quit ) ")
parser.add_argument("--task", help="Task to add")
parser.add_argument("--index", type=int, help="Index to remove or mark")


arg = parser.parse_args()
choice = arg.choose
print("Q or quit to close (type everything lower cased)")
if choice == "add":
    add_note()
elif choice == "remove":
    remove_note()
elif choice == "list":
    list_all()
elif choice == "mark":
    mark_done()
elif choice in ("q", "quit"):
    pass
else:
    print("Invalid choice.")'''
#---------------------------------------------------------------------------------------------------- final code with some ai help 


parser = argparse.ArgumentParser(description="CLI app")
parser.add_argument("--choose", help="Choose action: add, remove, list, mark, quit")
args = parser.parse_args()

#the help text that gets printed when command is triggered
help_text = """
Available commands:
  add     - Add a new note
  remove  - Remove a note by number
  list    - List all notes
  mark    - Mark a note as done
  quit/q  - Quit the application
  help/h  - Show this help message
"""

def process_choice(choice):#a function that does depends on the user input
    if choice == 'add':
        add_note()
    elif choice == 'remove':
        remove_note()
    elif choice == 'list':
        list_all()
    elif choice == 'mark':
        mark_done()
    elif choice in ('quit', 'q'):
        print("Goodbye!")
        return False  # stop loop
    elif choice in ('help', 'h'):
        print(help_text)
    else:
        print("Invalid choice. Type 'help' or 'h' to see available commands.")
    return True

print("Type 'quit' or 'q' to exit. Type 'help' or 'h' for help.")#a note for the user

if args.choose:
    # If argument given process it once and exit
    process_choice(args.choose.lower())
else:
    # No argument
    running = True
    while running:
        user_choice = input("Choose (add, remove, list, mark, quit): ").strip().lower()
        running = process_choice(user_choice)
