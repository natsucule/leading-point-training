import json
from operator import index

details=[]
contact={}
try:
    with open("Contacts.json", "r") as file:
         contact_json = json.load(file)

except (FileNotFoundError, json.JSONDecodeError):
    contact_json = {}
    print("json.JSONDecodeError")
#print(contact_json)

class contacts:
    def __init__(self):

        self.name = None
        self.phone = None
        self.email = None
        self.c_name = None
        self.find=None
        self.contact_json=None
        self.up=None




    def save_contacts(self):
        with open("Contacts.json", "w") as file:
            json.dump(contact, file, indent=4)

    def load_contact(self):
        with open("Contacts.json", "r") as file:
            try:
                with open("Contacts.json", "r") as file:
                    self.contact_json = json.load(file)
                    contact.update(self.contact_json)

            except (FileNotFoundError, json.JSONDecodeError):
                self.contact_json = {}
                print("json.JSONDecodeError")



    def add_contact(self,check="",reverse=""):
        res = self.load_contact()
        self.list_all()


        while True:


            print(
                "contact name")

            self.c_name = input("Enter contact name : ").lower()

            if self.c_name in contact.keys():
                print("this contact already exists")
                continue

            if not self.c_name.isalpha():
                print("Not a valid name please only enter letters")
                continue


            print("enter the name")
            self.name = input().lower()

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


            self.load_contact()


            details.append(f"Name: {self.name}")
            details.append(f"Phone Number: {self.phone}")
            details.append(f"Email: {self.email}")

            contact.update({self.c_name:details})
            self.save_contacts()



            break


    def list_all(self):
        self.load_contact()

        print("all contacts")
        if not contact:
            print("The list is empty.")
            return
        for i, con in enumerate(contact, start=1):  # add numbers to the start
            print(f"{i}. {con}")

        print("Contacts:")


        print(contact)




    def search(self):
        self.list_all()#search
        self.find=input("what u looking for?").lower()
        for i in contact:
            if self.find in contact.keys():
                print("*******************************************")
                print(contact[self.find])




    def delete_contact(self,confirmation=""):
        self.list_all()
        self.up = contact
        self.find = input("which contact you want to delete?").lower()
        if self.find in contact.keys():
            print(f"are you sure you want to delete {self.find} from your contacts? [Y/N]")
            confirmation = input().lower().strip()
            if confirmation == "y":
                del (self.up[self.find])
                contact.update(self.up)
                self.save_contacts()
                self.up.clear()
            elif confirmation == "n":
                pass
            else:
                print("invalid input")





    def modify_contact(self):
        self.list_all()
        self.up=contact
        self.find = input("which contact you want to modify?").lower()
        if self.find in contact.keys():
            del (self.up[self.find])
            contact.update(self.up)
            self.save_contacts()
            self.up.clear()
            self.add_contact()
            #contact.update(self.up)
            print(contact)
            self.save_contacts()


c=contacts()

'''
    def modify_contact(self):
        self.list_all()
        self.find = input("which contact you want to modify?").lower()
        if self.find in contact.keys():
            del (contact[self.find])
            self.add_contact()
            self.save_contacts()
            print(self.find)



c.load_contact()

#c.list_all()
#c.add_contact()
c.modify_contact()
#c.delete_contact()
#print(contact)
c.list_all()

'''
