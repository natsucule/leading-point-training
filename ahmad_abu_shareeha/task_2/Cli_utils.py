import json

details=[]
contact={}
hm=""
try:
    with open("Contacts.json", "r") as file:
        contact = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    contact ={}

class contacts:
    def __init__(self):

        self.name = None
        self.phone = None
        self.email = None
        self.c_name=None

    def save_contacts(self):
        with open("Contacts.json", "w") as file:
            json.dump(contact, file, indent=4)

    def add_contact(self):
        print("contact name")
        self.c_name = input("Enter contact name : ")

        print("enter the name")
        self.name = input()



        print("enter the phone number")
        self.phone = input()


        print("enter the email")
        self.email = input()


        details.append(f"Name: {self.name}")
        details.append(f"Phone: {self.phone}")
        details.append(f"Email: {self.email}")


        contact={self.c_name:details}

        with open("Contacts.json", "a") as file:
            json.dump(contact, file, indent=4)
        self.save_contacts()



       # contact.pop(self.c_name)  delete by name







    def list_all(self):
        if not details:
            print("The list is empty.")
            return
        for i, con in enumerate(contact, start=1):  # add numbers to the start
            print(f"{i}. {con}")

        print("Contacts:")






print(contact)












c=contacts()
c.add_contact()
c.list_all()
