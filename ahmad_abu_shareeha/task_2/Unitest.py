import unittest
from cli_utils import *

class TestContacts(unittest.TestCase):
    def setUp(self):
        contact.clear()

    def test_add_contact(self):
        contact["a"] = {"phone": "111", "email": "a@gmail.com"}
        self.assertIn("a", contact)
        self.assertEqual(contact["a"]["phone"], "111")
        self.assertEqual(contact["a"]["email"], "a@gmail.com")

    def test_search_contact(self):
        contact["b"] = {"phone": "22222", "email": "b@gmail.com"}
        found = "b" in contact
        self.assertTrue(found)
        self.assertEqual(contact["b"]["phone"], "22222")

    def test_delete_contact(self):
        contact["c"] = {"phone": "3333", "email": "c@gmail.com"}
        self.assertIn("c", contact)
        del contact["c"]
        self.assertNotIn("c", contact)

if __name__ == "__main__":
    unittest.main()
