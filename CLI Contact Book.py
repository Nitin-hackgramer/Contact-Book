import json


class Contact:
    """A class to represent a contact."""

    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def to_dict(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "address": self.address,
        }

    def __str__(self):
        return f"Name: {self.name} | Phone: {self.phone} | Email: {self.email} | Address: {self.address}"


class ContactBook:
    """
    A class to represent a contact book.

    Attributes:
        filename (str): The name of the file where contacts are stored.
        contacts (list): A list to store contact objects.

    Methods:
        add_contact(contact): Adds a contact to the contact list and saves it.
        search_contact(query): Searches for contacts that match the query.
        view_contact(): Prints all the contacts in the contact list.
        update_contact(old_name, new_name, new_email, new_phone, new_address): Updates the details of an existing contact.
        delete_contact(name): Deletes a contact from the contact list.
        save_contact(): Saves the contact list to a file.
        load_contact(): Loads the contact list from a file.
    """

    def __init__(self, filename="filename.json"):
        self.filename = filename
        self.contacts = []
        self.load_contact()

    def add_contact(self, contact):
        """Add Contact to the Contact List"""
        self.contacts.append(contact)
        self.save_contact()
        print("\n✅ Contact Added Successfully!")

    def search_contact(self, query):
        """Search Contact from the Contact List"""
        result = [c for c in self.contacts if query.lower() in c.name.lower() or query.lower() in c.phone.lower()
        ]
        if result:
            print("\n🔍 Search Results:")
            for contact in result:
                print(contact)
        else:
            print("\n⚠️ No Matching Contact Found!")

    def view_contact(self):
        """Print All the Contacts From the Contact list"""
        if self.contacts:
            print("\n📒 Contact List:")
            for idx, contact in enumerate(self.contacts, start=1):
                print(f"{idx}.{contact}")
        else:
            print("\n⚠️ No Contact Found!")

    def update_contact(self, old_name, new_name, new_email, new_phone, new_address):
        """Update the Contact"""
        for contact in self.contacts:
            if contact.name.lower() in old_name.lower():
                contact.name, contact.email, contact.phone, contact.address = (
                    new_name,
                    new_email,
                    new_phone,
                    new_address,
                )
                self.save_contact()
                print("\n✅ Contact Updated Successfully!")
            print("\n⚠️ Contact not found!")

    def delete_contact(self, name):
        """Delete the Contact from the Contact List"""
        self.contacts = [c for c in self.contacts if c.name.lower() != name.lower()]
        self.save_contact()
        print("\n🗑️ Contact Deleted Successfully!")

    def save_contact(self):
        """Save the Contact in the Contact list"""
        try:
            with open(self.filename, "w") as f:
                json.dump([c.to_dict() for c in self.contacts], f, indent=4)
        except IOError as e:
            print(f"❌ Error Saving Contact: {e}")

    def load_contact(self):
        """Load all the Contacts from the File"""
        try:
            with open(self.filename, "r") as f:
                contact_data = json.load(f)
                self.contacts = [Contact(**data) for data in contact_data]

        except FileNotFoundError:
            self.contacts = []
        
        except json.JSONDecodeError as e:
            print(f"❌ Error Loading Contact: {e}")
            contact = []


def main():
    """
    Main Function to Run the CLI Contact Book Program.
    This function provides a command-line interface for managing a contact book.
    It allows the user to perform the following operations:
    1. Add a new contact
    2. View all contacts
    3. Search for a contact by name or phone number
    4. Update an existing contact
    5. Delete a contact
    6. Exit the program
    The function runs in an infinite loop, prompting the user to choose an operation
    until the user decides to exit the program.
    """
    contactBook = ContactBook()

    while True:
        print("\nWelcome to the CLI Contact Book Program")
        print("1️⃣ to Add Contact")
        print("2️⃣ to View Contacts")
        print("3️⃣ to Search Contact")
        print("4️⃣ to Update Contact")
        print("5️⃣ to Delete Contact")
        print("6️⃣ to Exit the Program")

        choice = input("\n🔷 Enter Your Choice: ")

        if choice == "1":
            name = input("📛 Name: ")
            email = input("📧 Email: ")
            phone = input("📞 Phone: ")
            address = input("🏠 Address: ")
            contactBook.add_contact(
                Contact(name=name, email=email, phone=phone, address=address)
            )

        elif choice == "2":
            contactBook.view_contact()

        elif choice == "3":
            query = input("🔍 Enter name or phone no to search: ")
            contactBook.search_contact(query=query)

        elif choice == "4":
            old_name = input("📛 Enter existing contact name to update: ")
            new_name = input("📛 New Name: ")
            new_email = input("📧 New Email: ")
            new_phone = input("📞 New Phone: ")
            new_address = input("🏠 New Address: ")
            contactBook.update_contact(
                old_name=old_name,
                new_name=new_name,
                new_email=new_email,
                new_phone=new_phone,
                new_address=new_address,
            )

        elif choice == "5":
            name = input("🗑️ Enter name of contact to delete: ")
            contactBook.delete_contact(name=name)

        elif choice == "6":
            print("\n👋 Exiting Contact Book. Goodbye!")
            break

        else:
            print("\n❌ Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
