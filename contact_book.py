# ----------------------------------------
#  Project : Command-Line Contact Book
#  Language: Python
#  Storage : JSON
#  Developer: Shrilaxmi Shrichippa
# ----------------------------------------


import json
import os

FILE_NAME = "contact.json"

def load_contacts():

    if os.path.exists(FILE_NAME):
    
        try:
            with open(FILE_NAME, "r") as file:
               return json.load(file)
        
        except json.JSONDecodeError:
            print("Error reading contacts file. ")
            return []

    return []



def save_contacts(contacts):

    with open(FILE_NAME, "w") as file:

        json.dump(contacts, file, indent=4)

contacts = load_contacts()



def validate_phone(phone):

    if not phone.isdigit():
        print("\nPhone number should contain only digits.")
        return False

    if len(phone) != 10:
        print("\nPhone number must contain exactly 10 digits.")
        return False

    return True



def validate_email(email):

    if "@" not in email:
        print("\nEmail must contain '@'.")
        return False
    
    if "." not in email:
         print("\nEmail must contain '.'.")
         return False
    
    return True



def is_duplicate(contacts, phone, email):

    for contact in contacts:

        if contact["phone"] == phone:
            print("\nThis phone number already exists.")
            return True
        
        if contact["email"].lower() == email.lower():
            print("\nThis email already exists.")
            return True
        
    return False



def add_contact(contacts):

    name = input("Enter Name:")

    while True:
         phone = input("Enter Phone Number: ")
         if validate_phone(phone):
             break
         
    while True:
        email = input("Enter Email Address: ")
        if validate_email(email):
            break

    if is_duplicate(contacts, phone, email):
        return
    
    contact = {
        "name" : name,
        "phone" : phone,
        "email" : email
    }

    contacts.append(contact)
    save_contacts(contacts)

    print("\n Contact added successfully!")



def view_contact(contacts):

    if not contacts:

        print("\nNo contacts found!")
        return
    
    print("\n===== CONTACT LIST =====")
    for index, contact in enumerate(contacts, start=1):
        print(f"\nContact {index}:")
        print(f"Name : {contact['name']}")
        print(f"Phone : {contact['phone']}")
        print(f"Email : {contact['email']}")
        print("-" * 20)
    



def search_contact(contacts):

    search = input("Enter the Name or Phone Number: ")

    for contact in contacts:

        if (search.lower() in contact["name"].lower() or 
            search in contact["phone"]):
            
            print("\nContact Found!")
            print(f"Name : {contact['name']}")
            print(f"Phone : {contact['phone']}")
            print(f"Email : {contact['email']}")
            return
        
    print("\nContact not found!")



def update_contact(contacts):

    search = input("Enter Name or Phone Number to update:")

    for contact in contacts:

        if (contact["name"].lower() == search.lower() or 
                contact["phone"] == search):
            
            print("\n Contact Found!")
            print(f"Current Name : {contact['name']}")
            print(f"Current phone : {contact ['phone']}")
            print(f"Current Email : {contact ['email']}")

            contact["name"] = input("Enter New Name: ")
            
            while True:
                new_phone = input("Enter New Phone number: ")
                if validate_phone(new_phone):
                    contact["phone"] = new_phone
                    break

            while True:
                new_email = input("Enter New Email: ")
                if validate_email(new_email):
                    contact["email"] = new_email
                    break

            save_contacts(contacts)
            print("\n Contact updated Successfully!") 
            return
    print("\n Contact Not Found!")  



def delete_contact(contacts):

    search = input("Enter Name or Phone Number to delete: ")

    for contact in contacts:

        if (contact["name"].lower() == search.lower() or
                contact["phone"] == search):

            print("\nContact Found!")
            print(f"Name  : {contact['name']}")
            print(f"Phone : {contact['phone']}")
            print(f"Email : {contact['email']}")

            confirm = input("\nAre you sure you want to delete this contact? (yes/no): ")

            if confirm.lower() == "yes":
                contacts.remove(contact)
                save_contacts(contacts)

                print("\nContact Deleted Successfully!")
            else:
                print("\nDeletion Cancelled!")

            return

    print("\nContact Not Found!")
        


def sort_contacts(contacts, sort_by):

    if len(contacts) == 0:
        print("\nNo contacts found!")
        return
    
    if sort_by == "name":
         contacts.sort(key=lambda contact: contact["name"].lower())
         
    elif sort_by == "phone":
        contacts.sort(key=lambda contact: contact["phone"])

    save_contacts(contacts)

    print("\nContacts sorted successfully!")



while True: 
    print("\n======================= \nCONTACT BOOK \n=======================")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Sort By Name")
    print("7. Sort By Phone Number")
    print("8. Exit")
    print("========================\n")

    choice = input("Enter your choice (1-8): ")

    if choice == '1':
        add_contact(contacts)

    elif choice == '2':
        view_contact(contacts)

    elif choice == '3':
        search_contact(contacts)

    elif choice == '4':
        update_contact(contacts)

    elif choice == '5':
        delete_contact(contacts)

    elif choice == '6':
        sort_contacts(contacts, sort_by="name")

    elif choice == '7':
        sort_contacts(contacts, sort_by="phone")

    elif choice == '8':
        print("Thank you for using Contact Book!")
        break
    else:
        print("Invalid Choice!")
