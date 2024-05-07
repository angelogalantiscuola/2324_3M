"""
Esercizio 1

Dato i seguenti valori inseriti in input:
- Nome di un alunno
- Tre voti di una materia
Il compito è calcolare e visualizzare la media dei voti.
"""

nome = input("Inserisci il nome dell'alunno: ")
voto1 = int(input("Inserisci il primo voto: "))
voto2 = int(input("Inserisci il secondo voto: "))
voto3 = int(input("Inserisci il terzo voto: "))

media = (voto1 + voto2 + voto3) / 3

print(f"La media dei voti di {nome} è {media}")
