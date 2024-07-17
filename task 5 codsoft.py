class Contact:
    def __init__(self, name, phone, email="", address=""):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
class ContactBook:
    def __init__(self):
        self.contacts = {}
    def add_or_update_contact(self, name, phone, email="", address=""):
        self.contacts[name.lower()] = Contact(name, phone, email, address)
        print(f"Contact {name} {'updated' if name.lower() in self.contacts else 'added'} successfully.")
    def view_contacts(self):
        if not self.contacts:
            print("Contact book is empty.")
        else:
            print("Contact List:")
            for contact in self.contacts.values():
                print(f"Name: {contact.name}, Phone: {contact.phone}")
    def search_contact(self, query):
        query = query.lower()
        return [contact for contact in self.contacts.values() 
                if query in contact.name.lower() or query in contact.phone]
    def delete_contact(self, name):
        if name.lower() in self.contacts:
            del self.contacts[name.lower()]
            print(f"Contact {name} deleted successfully.")
        else:
            print(f"Contact {name} not found.")
def get_input(prompt, required=True):
    while True:
        value = input(prompt).strip()
        if value or not required:
            return value
def main():
    contact_book = ContactBook()
    actions = {
        '1': ('Add/Update Contact', lambda: contact_book.add_or_update_contact(
            get_input("Enter name: "),
            get_input("Enter phone number: "),
            get_input("Enter email (optional): ", required=False),
            get_input("Enter address (optional): ", required=False)
        )),
        '2': ('View Contacts', contact_book.view_contacts),
        '3': ('Search Contact', lambda: print("\n".join(
            f"Name: {c.name}, Phone: {c.phone}" for c in 
            contact_book.search_contact(get_input("Enter name or phone number to search: "))
        ) or "No contacts found.")),
        '4': ('Delete Contact', lambda: contact_book.delete_contact(get_input("Enter name of contact to delete: "))),
        '5': ('Exit', exit)
    }
    while True:
        print("\nContact Book Menu:")
        for key, (action, _) in actions.items():
            print(f"{key}. {action}")

        choice = input("Enter your choice: ")
        if choice in actions:
            actions[choice][1]()
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
