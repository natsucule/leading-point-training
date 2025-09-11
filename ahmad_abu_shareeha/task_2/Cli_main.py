 from Cli_utils import *
import argparse
if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="CLI app")
    parser.add_argument("--choose", help="Choose action: add, delete, list, modify, quit")
    args = parser.parse_args()

    # the help text that gets printed when command is triggered
    help_text = """
    Available commands:
      add     - Adds a new contact
      delete  - Deletes the chosen contact
      list    - List all contacts
      modify    - modifies the chosen contact
      quit/q  - Quit the application
      help/h  - Show this help message
    """

    def process_choice(choice):
        if choice == 'add':
            c.add_contact()
        elif choice == 'delete':
            c.delete_contact()
        elif choice == 'list':
            c.list_all()
        elif choice == 'modify':
            c.modify_contact()
        elif choice in ('quit', 'q'):
            print("Goodbye!")
            return False  # stop loop
        elif choice in ('help', 'h'):
            print(help_text)
        else:
            print("Invalid choice. Type 'help' or 'h' to see available commands.")
        return True


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