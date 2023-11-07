#Scrivere 10 volte la parola "ciao", sommare i numeri da 10 a 20 (compresi gli estremi), sommare i numeri pari fino a 30 (30 incluso) e moltiplicare i numeri da 1 a 10

for _ in range(10):
    print("ciao")

somma1 = range(11,21)
print("Somma dei numeri da 10 a 20:",somma1)

somma2 = range(1,31,2)
print("Somma dei numeri pari fino a 30:",somma2)

prodotto = 1
for i in range(1,11):
    prodotto *= i 
    print("Prodotto numeri da 1 a 11",prodotto)