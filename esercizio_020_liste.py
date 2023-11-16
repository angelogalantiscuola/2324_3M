import os # operating system

items = ["fragole", "banane", "mele"]
quantities = [3, 5, 2]


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
    choice = input("Scelta:")
    match choice:
        case '1':
            for item, quantity in zip(items, quantities):
                print(f"{item}: {quantity}")
        case '2':
            item = input("Enter the item: ")
            quantity = int(input("Enter the quantity: "))
            items.append(item)
            quantities.append(quantity)
        case '3':
            item = input("Enter the item: ")
            if item in items:
                quantity = int(input("Enter the new quantity: "))
                index = items.index(item)
                quantities[index] = quantity
            else:
                print("Item not found.")
        case '4':
            item = input("Enter the item: ")
            if item in items:
                index = items.index(item)
                items.pop(index)
                quantities.pop(index)
            else:
                print("Item not found.")
        case '5':
            break
        case _:
            print("Invalid choice.")
    input("Press enter to continue...")
