# Esercizio 19
# Dato in input un numero scritto con sistema di numerazione decimale (intero), 
# calcolare la sua conversione in binario. 
# Dato che la stampa a video del numero deve avvenire in ordine inverso 
# da quello del calcolo, usare una lista per stampare il valore corretto.

numero_decimale = int(input("Inserisci un numero: "))
numero_binario = []
risultato_della_divisione = numero_decimale
while not(risultato_della_divisione == 0):
    resto = risultato_della_divisione % 2 # resto della divisione
    risultato_della_divisione = risultato_della_divisione // 2 # risultato della divisione intera
    numero_binario.append(resto)
    print(numero_binario)
# invertire la lista
numero_binario.reverse()

print(f'il numero {numero_decimale} convertito in binario vale: {numero_binario}')
# stampare il numero binario in modo carino
for cifra in numero_binario:
    print(cifra, end='')
