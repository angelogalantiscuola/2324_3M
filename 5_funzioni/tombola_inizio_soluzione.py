"""
Gioco della tombola o del bingo
"""

import random

"""
La funzione genera una cartella della tombola/bingo e la restituisce come dizionario. 
Dare un id alla cartella.
N.B.
La cartella ha le seguenti caratteristiche:
1) 3 righe e 9 colonne
2) 15 numeri in totale (5 per riga)
3) ogni colonna ha solo i numeri della decina di riferimento: 
la prima dall'1 al 10, la seconda dal 11 al 20....l'ultima dall'81 al 90
"""
def genera_cartella(id: int) -> dict:
    cartella = []

    for indice_colonna in range(9):
        colonna = []
        # for j in range(3): # non so a priori quanti numeri devo generare
        while len(colonna) < 3:
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
    # print(cartella)

    # trasformare la lista di colonne in una lista di righe
    cartella_righe = []
    for i in range(3):  # 3 righe
        riga = []  # riga vuota
        for colonna in cartella:  # per ogni colonna (lista di 3 elementi)
            riga.append(colonna[i])
        cartella_righe.append(riga)

    # print(cartella_righe)

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


    # print(cartella_righe)

    # trasformare la lista di righe in un dizionario
    cartella_dict = {
        "id": id,
        "righe": cartella_righe
    }

    return cartella_dict

"""
La funzione estrae un nuovo numero, lo inserisce nella lista passata come parametro, 
controllando che non sia duplicato, e restituisce tale numero come intero.
"""
def estrai_numero(numeri_estratti: list[int]) -> int:
    numero = random.randint(1, 90)
    while numero in numeri_estratti:
        numero = random.randint(1, 90)
    numeri_estratti.append(numero)
    return numero


'''
Data come parametro una cartella e la lista di numeri estratti restituisca lo stato di tale cartella. 
Potrebbe restituire una lista di bool dove l'elemento 0 si riferisce all'ambo, 
l'1 al terno fino ad arrivare al 4 che si riferisce alla tombola/bingo.
es.
[True, True, False, False, False] per una cartella che ha fatto terno 
(naturalmente per fare terno bisogna aver fatto anche ambo....)
'''
def controlla_cartella(cartella: dict, numeri_estratti:list[int]) -> list[bool]:
    pass


# logica di funzionamento
# variabili di stato 
# (es. una lista di cartelle, la lista dei numeri estratti, lo stato del gioco(ambo, terno,....))
numeri_estratti = []
cartelle = [genera_cartella(1), genera_cartella(2), genera_cartella(3)]
numero_estratto = estrai_numero(numeri_estratti)
print(numero_estratto)
print(numeri_estratti)
numero_estratto = estrai_numero(numeri_estratti)
print(numero_estratto)
print(numeri_estratti)
