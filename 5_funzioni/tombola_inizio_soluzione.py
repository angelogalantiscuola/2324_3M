# Sulla base di quanto visto a lezione sul modulo random realizzare un programma che implementi il gioco della tombola o del bingo.
# Al fine di far ciò, lo studente implementi le seguenti funzioni:
# 1) def genera_cartella(id: int<str>)->dict:
# La funzione genera una cartella della tombola/bingo e la restituisce come dizionario. Dare un id alla cartella.
# N.B.
# La cartella ha le seguenti caratteristiche:
# 1) 3 righe e 9 colonne
# 2) 15 numeri in totale (5 per riga)
# 3) ogni colonna ha solo i numeri della decina di riferimento: la prima dall'1 al 10, la seconda dal 11 al 20....l'ultima dall'81 al 90


# 2) def estrai_numero(numeri_estratti: list[])->int:
# La funzione estrae un nuovo numero, lo inserisce nella lista passata come parametro, controllando che non sia duplicato, e restituisce tale numero come intero.

# 0 --> 0*10 = 0, 0*10+9 = 9
# 1 --> 1*10 = 10, 1*10+9 = 19
# 2 --> 2*10 = 20, 2*10+9 = 29

# numero_casuale = random.randint(1, 9)  # 9 numeri
# numero_casuale = random.randint(10, 19) # 10 numeri
# numero_casuale = random.randint(20, 29) # 10 numeri
# numero_casuale = random.randint(80, 90) # 11 numeri

import random


cartella = []

for indice_colonna in range(9):
    colonna = []
    # for j in range(3): # non so a priori quanti numeri devo generare
    while len(colonna) < 3:
        print(f"colonna {indice_colonna}")
        if indice_colonna == 0:
            numero_casuale = random.randint(indice_colonna * 10 + 1, indice_colonna * 10 + 9)
        elif indice_colonna == 8:
            numero_casuale = random.randint(indice_colonna * 10, indice_colonna * 10 + 10)
        else:
            numero_casuale = random.randint(indice_colonna * 10, indice_colonna * 10 + 9)
        # controllo se il numero è già presente nella colonna
        if numero_casuale not in colonna:
            colonna.append(numero_casuale)
    cartella.append(colonna)
print(cartella)

# trasformare la lista di colonne in una lista di righe
cartella_righe = []
for i in range(3):  # 3 righe
    riga = []  # riga vuota
    for colonna in cartella:  # per ogni colonna (lista di 3 elementi)
        riga.append(colonna[i])
    cartella_righe.append(riga)

print(cartella_righe)

# # mettere a 0 4 numeri per ogni riga
# for riga in cartella_righe:
#     count_zeros = 0
#     while count_zeros < 4:
#         indice = random.randint(0, 8)
#         if riga[indice] != 0:
#             riga[indice] = 0
#             count_zeros += 1

# mettere a 0 4 numeri per ogni riga: soluzione migliore usando random.choice
for riga in cartella_righe:
    for _ in range(4):
        indice = random.choice(range(9))
        riga[indice] = 0

# # mettere a 0 4 numeri per ogni riga: soluzione migliore usando random.sample
# for riga in cartella_righe:
#     numeri_da_cancellare = random.sample(range(9), 4)
#     for indice in numeri_da_cancellare:
#         riga[indice] = 0


print(cartella_righe)


# 3) def controlla_cartella(cartella: dict, numeri_estratti[])->list[bool]:
# Data come parametro una cartella e la lista di numeri estratti restituisca lo stato di tale cartella. Potrebbe restituire una lista di bool dove l'elemento 0 si riferisce all'ambo, l'1 al terno fino ad arrivare al 4 che si riferisce alla tombola/bingo.
# es.
# [True, True, False, False, False] per una cartella che ha fatto terno(naturalmente per fare terno bisogna aver fatto anche ambo....)

# Realizzare un programma che implementi la logica di funzionamento:
# a) Utilizzando le opportune variabili di stato (es. una lista di cartelle, la lista dei numeri estratti, lo stato del gioco(ambo, terno,....))
# b) Utilizzando le funzioni precedentemente definite al fine di gestire le varie fasi del gioco.
