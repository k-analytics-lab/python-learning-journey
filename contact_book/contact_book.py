print(10*"-","Contact Book",10*"-")

contacts={}

while True:
    print("1.Add\n2.View\n3.Search\n4.Delete\n5.Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("Enter the name: ")
        number = int(input("Enter the number: "))
        contacts[name] = number
        print("Contact added!\n")
    elif choice == 2:
        print(5*"-","Contact List",5*"-")
        if not contacts:
                print("No Contacts!")
        else:
            for name,num in contacts.items():
                print(f"{name} -> {num}")
    elif choice == 3:
        name = input("Search contacts: ")
        if name in contacts:
            print(name,contacts[name])
            print()
        else:
            print("Contact not found!\n")
    elif choice == 4:
        delete = input("Enter the contact u wanna delete: ")
        if delete in contacts:
            contacts.pop(delete)
            print("Contact Deleted Successfully!")
        else:
            print("Contact not found!\n")
    elif choice == 5:
        print("Do you wanna exit program: (Yes/NO)\n")
        decision = input("").lower()
        if decision == "yes":
            print("Exiting Program...")
            break
        else:
            continue




        


