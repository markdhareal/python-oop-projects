from book_model import ContactBook
from contact_model import Contact

if __name__ == '__main__':
    contact_book = ContactBook()
    contact1 = Contact("John Doe", "123-456-7890", "john@example.com")
    contact2 = Contact("Jane Smith", "098-765-4321", "jane@example.com")
    contact_book.add_contact(contact1)
    contact_book.add_contact(contact2)

    contact_book.list_contacts()
    contact_book.search_contact("John Doe")
    contact_book.delete_contact("Jane Smith")
    contact_book.list_contacts()