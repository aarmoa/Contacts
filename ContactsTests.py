from Contacts import ContactsList, contacts
import unittest

class ContacListTest(unittest.TestCase):

    def test_noMatchesOnEmptyContactList(self):
        contactList = ContactsList()
        self.assertEqual(contactList.matchesNumberForPrefix('a'), 0)

    def test_oneMatchingContact(self):
        contactList = ContactsList()
        contactList.addContact('hack')
        contactList.addContact('hackerrank')
        self.assertEqual(contactList.matchesNumberForPrefix('hacke'), 1)

    def test_twoMatchingContacts(self):
        contactList = ContactsList()
        contactList.addContact('hack')
        contactList.addContact('hackerrank')
        self.assertEqual(contactList.matchesNumberForPrefix('hack'), 2)

class ContactsTest(unittest.TestCase):

    def test_findOnEmptyContactsListReturnsNoResults(self):
        queries = []
        queries.append(['find', 'hac'])
        self.assertEqual(contacts(queries), [0])

    def test_mixedAddAndFindCommandsReturnTwoResults(self):
        queries = []
        queries.append(['add', 'hack'])
        queries.append(['find', 'hac'])
        queries.append(['add', 'hackerranck'])
        queries.append(['find', 'hac'])
        queries.append(['find', 'hak'])
        self.assertEqual(contacts(queries), [1, 2, 0])


if __name__ == '__main__':
    unittest.main()