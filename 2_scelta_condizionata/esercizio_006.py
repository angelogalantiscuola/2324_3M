

def main():
    n1 = input("Inserisci il primo numero: ")
    n2 = input("Inserisci il secondo numero: ")

    n1 = int(n1)
    n2 = int(n2)

    if n1 % 2 == 0 and n2 % 2 == 0:  
        print("Entrambi i numeri sono pari")
    elif n1 % 2 != 0 and n2 % 2 != 0:  
        print("Tutti i numeri sono dispari")
    else: 
        print("Un numero è pari e l'altro è dispari")


if __name__ == "__main__":
    main()
