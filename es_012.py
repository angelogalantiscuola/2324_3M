#Dati in input n valori, calcolarne la somma.
#Suggerimenti....
#Si chieda quanti valori si vogliono inserire quando inizia il programma, si inizializzi la variabile di somma a zero prima che inizi il ciclo.

n = int(input("Inserisci il numero di valori da sommare:"))
somma = 0

for i in range(n):
    valore = float(input("Inserisci il valore:"))
    somma += valore 

    print(f"La somma dei {n} valori inseriti è: {somma}")