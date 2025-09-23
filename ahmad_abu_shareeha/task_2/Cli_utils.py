import json

details = []
contact = {}

try:
    with open("Contacts.json", "r") as file:
        contact_json = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    contact_json = {}
    print("json.JSONDecodeError")
    contact = {}

class contacts:
    def __init__(self):
        self.name = None
        self.phone = None
        self.email = None
        self.find = None
        self.contact_json = None

    def save_contacts(self):
        with open("Contacts.json", "w") as file:
            json.dump(contact, file, indent=4)

    def load_contact(self):
        try:
            with open("Contacts.json", "r") as file:
                self.contact_json = json.load(file)
                contact.update(self.contact_json)
        except (FileNotFoundError, json.JSONDecodeError):
            self.contact_json = {}
            print("json.JSONDecodeError")

    def add_contact(self, check="", reverse=""):
        self.load_contact()
        self.list_all()

        while True:
            self.name = input("Enter contact name: ").strip().lower()
            if not self.name.isalpha():
                print("Not a valid name, please only enter letters")
                continue
            if self.name in contact.keys():
                print("This contact already exists")
                continue
            
            break

        while True:
            self.phone = input("Enter phone number: ").strip()
            if not self.phone.isdigit():
                print("Not a valid phone number")
                continue
            break

        while True:
            self.email = input("Enter email: ").strip().lower()
            check = self.email
            reverse = ""
            for i in check[::-1]:
                reverse += str(i)
                if len(reverse) == 10:
                    break
            if reverse[::-1] != "@gmail.com":
                print("Invalid email, must end with (@gmail.com)")
                continue
            break

        details.clear()
        details.append(f"Phone Number: {self.phone}")
        details.append(f"Email: {self.email}")
        contact[self.name] = details
        self.save_contacts()
        print(f"Contact '{self.name}' added successfully!")

    def list_all(self):
        self.load_contact()
        print("All contacts:")
        if not contact:
            print("The list is empty.")
            return
        for i, con in enumerate(contact, start=1):
            print(f"{i}. {con}")
        print("Contacts:", contact)

    def search(self):
        self.list_all()
        self.find = input("What are you looking for? ").lower()
        matches = [(i, name, info) for i, (name, info) in enumerate(contact.items(), start=1) if self.find in name.lower()]
        if not matches:
            print(f"No contact found matching '{self.find}'")
            return
        print("Matching contacts:")
        for num, name, info in matches:
            print(f"{num}. {name} | {info}")
        if len(matches) > 1:
            chosen = int(input("Enter the number of the contact to view: "))
            for num, name, info in matches:
                if num == chosen:
                    print("Selected contact:")
                    print(f"{name} | {info}")
                    break
        else:
            print("Contact details:")
            print(f"{matches[0][1]} | {matches[0][2]}")

    def delete_contact(self):
        self.list_all()
        self.find = input("Which contact you want to delete? ").lower()
        matches = [(i, name, info) for i, (name, info) in enumerate(contact.items(), start=1) if self.find in name.lower()]
        if not matches:
            print(f"No contact found matching '{self.find}'")
            return
        print("Matching contacts:")
        for num, name, info in matches:
            print(f"{num}. {name} | {info}")
        if len(matches) > 1:
            chosen = int(input("Enter the number of the contact to delete: "))
            for num, name, info in matches:
                if num == chosen:
                    del contact[name]
                    self.save_contacts()
                    print(f"{name} deleted successfully.")
                    break
        else:
            del contact[matches[0][1]]
            self.save_contacts()
            print(f"{matches[0][1]} deleted successfully.")

    def modify_contact(self):
        self.list_all()
        self.find = input("Which contact you want to modify? ").lower()
        matches = [(i, name, info) for i, (name, info) in enumerate(contact.items(), start=1) if self.find in name.lower()]
        if not matches:
            print(f"No contact found matching '{self.find}'")
            return
        print("Matching contacts:")
        for num, name, info in matches:
            print(f"{num}. {name} | {info}")
        if len(matches) > 1:
            chosen = int(input("Enter the number of the contact to modify: "))
            for num, name, info in matches:
                if num == chosen:
                    index_name = name
                    break
        else:
            index_name = matches[0][1]
        del contact[index_name]
        self.add_contact()
        self.save_contacts()
        print(contact)

c = contacts()
# Example usage:
# c.add_contact()
# c.list_all()
# c.search()
# c.modify_contact()
# c.delete_contact()
