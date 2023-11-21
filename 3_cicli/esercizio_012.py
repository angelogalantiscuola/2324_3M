#Dati in input n valori, calcolarne la somma.
#Suggerimenti....
#Si chieda quanti valori si vogliono inserire quando inizia il programma, si inizializzi la variabile di somma a zero prima che inizi il ciclo.
valori=int(input("quanti valori da sommare:"))
somma=0

for i in range(valori):
    valore=int(input("inserisci valore: "))
    somma+=valore
print(f"la somma è {somma}")
    
