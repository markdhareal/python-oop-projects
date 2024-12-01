class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        return f"Contact '{contact.name}' is added."
    
    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                return f"Contact '{contact.name}' is deleted"
            
        return f"Contact '{contact.name}' not found."
    
    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return f"Contact '{contact.name}' is here."
            
        return f"Contact '{contact.name}' not found."
    
    def list_contacts(self):
        if not self.contacts:
            return 'No contacts available.'
        for contact in self.contacts:
            print(f"Name: {contact.name} - Phone: {contact.phone} - Email: {contact.email}")