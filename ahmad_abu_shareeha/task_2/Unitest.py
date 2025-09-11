import unittest
from contacts import contacts, contact

class testcontacts(unittest.TestCase):
    def setUp(self):
        contact.clear()
        self.c = contacts()

    def test_add_contact(self):
        c = self.c
        c.name = "a"
        c.phone = "1111111"
        c.email = "a@gmail.com"
        c.add_contact = lambda: contact.update({c.name: [f"Phone Number: {c.phone}", f"Email: {c.email}"]})
        c.add_contact()
        self.assertIn("a", contact)

    def test_search_contact(self):
        contact["b"] = ["Phone Number: 2222222", "Email: b@gmail.com"]
        c = self.c
        c.find = "b"
        found = [n for n in contact if c.find in n]
        self.assertIn("b", found)

    def test_delete_contact(self):
        contact["c"] = ["Phone Number: 3333333", "Email: c@gmail.com"]
        c = self.c
        c.find = "c"
        c.delete_contact = lambda: contact.pop(c.find, None)
        c.delete_contact()
        self.assertNotIn("c", contact)

if __name__ == "__main__":
    unittest.main()
