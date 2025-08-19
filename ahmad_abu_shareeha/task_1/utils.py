import json


todo_file = "todo.json"


# Try to load existing notes
try:
    with open(todo_file, "r") as file:
        notes = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    pass

# Save updated notes back to file
def save_notes():
    with open(todo_file, "w") as file:
        json.dump(notes, file, indent=4)
#-----------------------------------------------------------------------------
# Add a new note
def add_note():
    note = input("Enter note: ")
    notes.append(note)
    save_notes()

# -----------------------------------------------------------------------------
def remove_note():
    list_all()
    try:
        index = int(input("Enter number of note to delete: ")) - 1
        if 0 <= index < len(notes):
            removed = notes.pop(index)
            save_notes()
            print(f"Removed: {removed}")
        else:
            print(" Not valid number.")
    except ValueError:
        print(" Not valid number")

#-----------------------------------------------------------------------------
def mark_done():
    try:
        index = int(input("Enter the number of Done task: ")) - 1
        if 0 <= index < len(notes):
            notes[index] =  notes[index]+"( DONE)"
            save_notes()
            print(notes[index])
        else:
            print(" Not valid number.")
    except ValueError:
        print(" Not valid number.")
#-----------------------------------------------------------------------------
def list_all():
    if not notes:
        print("The list is empty.")
        return
    for i, note in enumerate(notes,start=1):#add numbers to the start
        print(f"{i}. {note}")

    print("Notes:")



