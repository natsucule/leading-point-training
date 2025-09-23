<<<<<<< HEAD
from cli_utils import *

=======
from Cli_utils import *
import argparse
>>>>>>> d36b3dfb009516a2d0ae1aab0fe127f5ca29290b
if __name__ == '__main__':
    help_text = """
Available commands:
  add     - Adds a new contact
  delete  - Deletes the chosen contact
  list    - List all contacts
  modify  - Modifies the chosen contact
  search  - Search contact by name
  quit/q  - Quit the application
  help/h  - Show this help message
"""

    def process_choice(choice):
        if choice == 'add':
            add_contact()
        elif choice == 'delete':
            delete_contact()
        elif choice == 'list':
            list_all()
        elif choice == 'modify':
            modify_contact()
        elif choice == 'search':
            name_search()
        elif choice in ('quit', 'q'):
            print("Goodbye!")
            return False
        elif choice in ('help', 'h'):
            print(help_text)
        else:
            print("Invalid choice. Type 'help' or 'h' to see available commands.")
        return True

<<<<<<< HEAD
    print("Type 'quit' or 'q' to exit. Type 'help' or 'h' for help.")
    running = True
    while running:
        user_choice = input("Choose (add, delete, list, modify, search, quit): ").strip().lower()
        running = process_choice(user_choice)
=======

    print("Type 'quit' or 'q' to exit. Type 'help' or 'h' for help.")  # a note for the user

    if args.choose:
        # If argument given process it once and exit
        process_choice(args.choose.lower())
    else:
        # No argument
        running = True
        while running:
            user_choice = input("Choose (add, delete, list, modify, quit): ").strip().lower()
            running = process_choice(user_choice)
>>>>>>> d36b3dfb009516a2d0ae1aab0fe127f5ca29290b
