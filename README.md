# CLI Contact Book

## Overview
The CLI Contact Book is a command-line interface application for managing a contact book. It allows users to add, view, search, update, and delete contacts. The contacts are stored in a JSON file, ensuring data persistence across sessions.

## Features
- **Add Contact**: Add a new contact with name, phone number, email, and address.
- **View Contacts**: Display all contacts in the contact book.
- **Search Contact**: Search for contacts by name or phone number.
- **Update Contact**: Update the details of an existing contact.
- **Delete Contact**: Remove a contact from the contact book.
- **Exit Program**: Exit the application gracefully.

## Usage
1. **Run the Program**: Execute the script to start the CLI Contact Book.
2. **Choose an Operation**: Select an operation from the menu by entering the corresponding number.
3. **Follow Prompts**: Enter the required information as prompted by the application.

## Code Structure
- **Contact Class**: Represents a contact with attributes for name, phone, email, and address.
- **ContactBook Class**: Manages the contact list, including adding, viewing, searching, updating, and deleting contacts. It also handles saving and loading contacts from a JSON file.
- **Main Function**: Provides the command-line interface for interacting with the contact book.

## Example
```sh
Welcome to the CLI Contact Book Program
1️⃣ to Add Contact
2️⃣ to View Contacts
3️⃣ to Search Contact
4️⃣ to Update Contact
5️⃣ to Delete Contact
6️⃣ to Exit the Program

🔷 Enter Your Choice: 1
📛 Name: John Doe
📞 Email: john.doe@example.com
📧 Phone: 1234567890
🏠 Address: 123 Main St
✅ Contact Added Successfully!
