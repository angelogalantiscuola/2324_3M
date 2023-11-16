import os

inventory = {"fragole": 5, "banane": 2}

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
    Scegliere l'opzione desiderata:
    1) Visualizza lista
    2) Aggiungi item e quantità
    3) Modifica quantità di un item
    4) Rimuovi item
    5) Esci
    Scelta:""")
    choice = input()
    if choice == '1':
        for item, quantity in inventory.items():
            print(f"{item}: {quantity}")
    elif choice == '2':
        item = input("Enter the item: ")
        quantity = int(input("Enter the quantity: "))
        inventory[item] = quantity
    elif choice == '3':
        item = input("Enter the item: ")
        if item in inventory:
            quantity = int(input("Enter the new quantity: "))
            inventory[item] = quantity
        else:
            print("Item not found.")
    elif choice == '4':
        item = input("Enter the item: ")
        if item in inventory:
            del inventory[item]
        else:
            print("Item not found.")
    elif choice == '5':
        break
    else:
        print("Invalid choice.")
    input("Press enter to continue...")