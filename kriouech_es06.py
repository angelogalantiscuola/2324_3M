numero1 = input("Inserisci il primo numero: ")
numero2 = input("Inserisci il secondo numero: ")

numero1 = int(numero1)
numero2 = int(numero2)


if numero1 % 2 == 0 and numero2 % 2 == 0:  
    risultato = "Entrambi i numeri sono pari"
elif numero1 % 2 == 1 and numero2 % 2 == 1:  
    risultato = "Entrambi i numeri sono dispari"
else:  
    risultato = "Uno dei numeri è pari e l'altro è dispari"

print(risultato)
