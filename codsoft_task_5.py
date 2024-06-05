# -*- coding: utf-8 -*-
"""codsoft_task_5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1jzBr2ZGrSsVisxluNj58bo8jf_mVeIVa
"""

import json

# File to store contacts
CONTACTS_FILE = "contacts.json"

def load_contacts():
    try:
        with open(CONTACTS_FILE, 'r') as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = []
    return contacts

def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    save_contacts(contacts)
    print("Contact added successfully!")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    print("\nContact List:")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']} - {contact['phone']}")

def search_contact(contacts):
    search_term = input("Enter name or phone number to search: ").lower()
    found_contacts = [contact for contact in contacts if search_term in contact['name'].lower() or search_term in contact['phone']]
    if found_contacts:
        for contact in found_contacts:
            print_contact(contact)
    else:
        print("No contact found.")

def print_contact(contact):
    print("\nName: ", contact['name'])
    print("Phone: ", contact['phone'])
    print("Email: ", contact['email'])
    print("Address: ", contact['address'])

def update_contact(contacts):
    search_term = input("Enter name or phone number to search for update: ").lower()
    for contact in contacts:
        if search_term in contact['name'].lower() or search_term in contact['phone']:
            print_contact(contact)
            print("\nEnter new details (leave blank to keep current):")
            name = input(f"Enter name ({contact['name']}): ") or contact['name']
            phone = input(f"Enter phone number ({contact['phone']}): ") or contact['phone']
            email = input(f"Enter email ({contact['email']}): ") or contact['email']
            address = input(f"Enter address ({contact['address']}): ") or contact['address']
            contact.update({"name": name, "phone": phone, "email": email, "address": address})
            save_contacts(contacts)
            print("Contact updated successfully!")
            return
    print("No contact found.")

def delete_contact(contacts):
    search_term = input("Enter name or phone number to delete: ").lower()
    for contact in contacts:
        if search_term in contact['name'].lower() or search_term in contact['phone']:
            contacts.remove(contact)
            save_contacts(contacts)
            print("Contact deleted successfully!")
            return
    print("No contact found.")

def main():
    contacts = load_contacts()
    while True:
        print("\nContact Book Menu")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()