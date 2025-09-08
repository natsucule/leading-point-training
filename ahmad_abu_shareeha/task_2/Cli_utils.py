import json
from operator import index

details=[]
contact={}

hm=""
con="Contacts.json"

try:
    with open(con, "r") as file:
        contact = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    contact = {}




class contacts:
    def __init__(self):

        self.name = None
        self.phone = None
        self.email = None
        self.c_name = None
        self.find=None

    def save_notes(self):
        with open("Contacts.json", "a") as file:
            json.dump(contact, file, indent=4)


    def add_contact(self,check="",reverse=""):
        self.list_all()

        while True:


            print("contact name")

            self.c_name = input("Enter contact name : ")
            if self.c_name in contact.keys():
                print("this contact already exists")
                continue

            if not self.c_name.isalpha():
                print("Not a valid name please only enter letters")
                continue


            print("enter the name")
            self.name = input()

            if  self.name=="":
                print("Not a valid name please only enter letters")
                continue


            print("enter the phone number")
            self.phone = input().strip()

            #if not self.phone.isdigit() or index(self.phone)!=7:
            if not self.phone.isdigit():
                print("Not a valid phone number(A phone number in jordan is only 7 digits)")

                continue



            print("enter the email")
            self.email = input().strip().lower()
            check=self.email

            for i in check[::-1]:
                reverse = str(reverse) + str(i)
                if len(reverse) == 10:
                    break

            if reverse[::-1] != "@gmail.com":
                print(f"invalid email it have to end with (@gmail.com)")

                continue

            details.clear()


            details.append(f"Name: {self.name}")
            details.append(f"Phone Number: {self.phone}")
            details.append(f"Email: {self.email}")

            contact.update({self.c_name:details})
            self.save_notes()


            break


    def list_all(self):
        if not contact:
            print("The list is empty.")
            return
        for i, con in enumerate(contact, start=1):  # add numbers to the start
            print(f"{i}. {con}")

        print("Contacts:")
        print(contact)



    def search(self):
        self.list_all()#search
        self.find=input("what u looking for?")
        for i in contact:
            if self.find in contact.keys():
                print("*******************************************")
                print(contact[self.find])




    def delete_contact(self,confirmation=""):
        self.list_all()
        self.find = input("which contact you want to delete?")
        for i in contact:
            if self.find in contact.keys():
                print(f"are you sure you want to delete {self.find} from your contacts? [Y/N]")
                confirmation = input().lower().strip()
                if confirmation == "y":
                    del (contact[self.find])
                    self.save_notes()
                elif confirmation == "n":
                    pass
                else:
                    print("invalid input")
                    continue


    def modify_contact(self):
        self.list_all()
        self.find = input("which contact you want to modify?")
        if self.find in contact.keys():
             del (contact[self.find])
             self.add_contact()
             self.save_notes()
             print(self.find)








c=contacts()
c.list_all()
#c.add_contact()
c.modify_contact()
#print(contact)