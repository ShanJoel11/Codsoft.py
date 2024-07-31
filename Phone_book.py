class ContactBook:
    def __init__(self):
        self.contacts = {}
    def add_contact(self, name, phone, email, address):
        self.contacts[name] = {"phone": phone, "email": email, "address": address}
        print(f"Contact {name} added successfully!")
    def view_contacts(self):
        if not self.contacts:
            print("No contacts saved.")
        else:
            for name, details in self.contacts.items():
                print(f"{name}: {details['phone']}")
    def search_contact(self, term):
        results = {name: details for name, details in self.contacts.items() 
                   if term.lower() in name.lower() or term in details['phone']}
        if results:
            for name, details in results.items():
                print(f"{name}: {details['phone']}, {details['email']}, {details['address']}")
        else:
            print("No matching contacts found.")
    def update_contact(self, name):
        if name in self.contacts:
            self.contacts[name]['phone'] = input("New phone (press enter to keep current): ") or self.contacts[name]['phone']
            self.contacts[name]['email'] = input("New email (press enter to keep current): ") or self.contacts[name]['email']
            self.contacts[name]['address'] = input("New address (press enter to keep current): ") or self.contacts[name]['address']
            print(f"Contact {name} updated successfully!")
        else:
            print("Contact not found.")
    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact {name} deleted successfully!")
        else:
            print("Contact not found.")
def main():
    book = ContactBook()
    while True:
        print("\nContact Book")
        print("1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Update Contact\n5. Delete Contact\n6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            book.add_contact(name, phone, email, address)
        elif choice == '2':
            book.view_contacts()
        elif choice == '3':
            term = input("Enter search term: ")
            book.search_contact(term)
        elif choice == '4':
            name = input("Enter name of contact to update: ")
            book.update_contact(name)
        elif choice == '5':
            name = input("Enter name of contact to delete: ")
            book.delete_contact(name)
        elif choice == '6':
            print("Exiting Contact Book...")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
