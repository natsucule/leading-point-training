from cli_utils import *

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

    print("Type 'quit' or 'q' to exit. Type 'help' or 'h' for help.")
    running = True
    while running:
        user_choice = input("Choose (add, delete, list, modify, search, quit): ").strip().lower()
        running = process_choice(user_choice)
