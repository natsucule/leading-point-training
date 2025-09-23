import json
# from validate_email import validate_email

contact = {}

def load_contact():
    try:
        with open("contacts.json", "r") as file:
            contact_json = json.load(file)
            contact.clear()
            contact.update(contact_json)
    except (FileNotFoundError, json.JSONDecodeError):
        contact.clear()

def save_contacts():
    with open("contacts.json", "w") as file:
        json.dump(contact, file, indent=4)

def add_contact():
    load_contact()
    list_all()

    while True:
        name = input("Enter contact name: ").strip()
        if not name.replace(" ", "").isalpha():
            print("Not a valid name, only letters and spaces are allowed")
            continue
        break

    while True:
        phone = input("Enter phone number: ").strip()
        if not phone.isdigit():
            print("Not a valid phone number")
            continue
        break

    while True:
        email = input("Enter email: ").strip()
        # Email validation temporarily disabled
        break

    contact[name] = {"phone": phone, "email": email}
    save_contacts()
    print(f"Contact '{name}' added successfully!")

def list_all():
    load_contact()
    print("All contacts:")
    if not contact:
        print("The list is empty.")
        return
    for x, con_name in enumerate(contact, start=1):
        con = contact[con_name]
        print(f"{x}. Name: {con_name} , Phone: {con['phone']} , Email: {con['email']}")

def delete_contact():
    load_contact()
    list_all()
    if not contact:
        return

    name = input("Which contact you want to delete? ").strip()
    if name in contact:
        del contact[name]
        save_contacts()
        print(f"{name} deleted successfully.")
    else:
        print(f"No contact found matching '{name}'")

def modify_contact():
    load_contact()
    list_all()
    if not contact:
        return

    name = input("Which contact you want to modify? ").strip()
    if name in contact:
        while True:
            new_name = input("Enter new name (leave empty to keep same): ").strip()
            if new_name and not new_name.replace(" ", "").isalpha():
                print("Not a valid name, only letters and spaces are allowed")
                continue
            
            break
        while True:
            phone = input("Enter new phone number: ").strip()
            if not phone.isdigit():
                print("Not a valid phone number")
                continue
            break
        while True:
            email = input("Enter new email: ").strip()
            # Email validation temporarily disabled
            break

        if new_name:
            contact[new_name] = {"phone": phone, "email": email}
            del contact[name]
            print(f"{name} modified successfully. Now saved as {new_name}.")
        else:
            contact[name] = {"phone": phone, "email": email}
            print(f"{name} modified successfully.")

        save_contacts()
    else:
        print(f"No contact found matching '{name}'")

def name_search():
    load_contact()
    if not contact:
        print("The list is empty.")
        return

<<<<<<< HEAD
    name = input("Enter name to search: ").strip()
    if name in contact:
        con = contact[name]
        print(f"Name: {name} , Phone: {con['phone']} , Email: {con['email']}")
    else:
        print(f"No contact found matching '{name}'")
=======
c = contacts()
# Example usage:
# c.add_contact()
# c.list_all()
# c.search()
# c.modify_contact()
# c.delete_contact()
>>>>>>> d36b3dfb009516a2d0ae1aab0fe127f5ca29290b
