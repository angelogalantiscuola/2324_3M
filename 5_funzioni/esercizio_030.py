#Sulla base di quanto visto a lezione sul modulo random realizzare un programma che implementi il gioco della tombola o del bingo. 
#Al fine di far ciò, lo studente implementi le seguenti funzioni:
#1) def genera_cartella(id: int<str>)->dict:
#La funzione genera una cartella della tombola/bingo e la restituisce come dizionario. Dare un id alla cartella.
#N.B.
#La cartella ha le seguenti caratteristiche:
#1) 3 righe e 9 colonne
#2) 15 numeri in totale (5 per riga)
#3) ogni colonna ha solo i numeri della decina di riferimento: la prima dall'1 al 9, la seconda dal 10 al 19....l'ultima dall'80 al 90
#
#
#2) def estrai_numero(numeri_estratti: list[])->int:
#La funzione estrae un nuovo numero, lo inserisce nella lista passata come parametro, controllando che non sia duplicato, e restituisce tale numero come intero.
#
#3) def controlla_cartella(cartella: dict, numeri_estratti[])->list[bool]:
#Data come parametro una cartella e la lista di numeri estratti restituisca lo stato di tale cartella.
#Potrebbe restituire una lista di bool dove l'elemento 0 si riferisce all'ambo, l'1 al terno fino ad arrivare al 4 che si riferisce alla tombola/bingo.
#es.
#[True, True, False, False, False] per una cartella che ha fatto terno(naturalmente per fare terno bisogna aver fatto anche ambo....)
#
#Realizzare un programma che implementi la logica di funzionamento:
#a) Utilizzando le opportune variabili di stato (es. una lista di cartelle, la lista dei numeri estratti, lo stato del gioco(ambo, terno,....))
#b) Utilizzando le funzioni precedentemente definite al fine di gestire le varie fasi del gioco.


import random

def genera_cartella(id:int):
    colonne = [[i for i in range(1, 10)],
                [i for i in range(10, 20)],
                [i for i in range(20, 30)],
                [i for i in range(30, 40)],
                [i for i in range(40, 50)],
                [i for i in range(50, 60)],
                [i for i in range(60, 70)],
                [i for i in range(70, 80)],
                [i for i in range(80, 91)]]

    righe = []
    
    for i in range(3):
        riga = []
        for x in range(9):
            numero = random.choice(colonne[x])
            colonne[x].pop(numero)
            riga.append(numero)
        righe.append(riga)

    for i in range(3):
        posizioni = [i for i in range(9)]
        for _ in range(4):
            posizione = random.choice(posizioni)
            posizioni.pop(posizione)
            righe[i][posizione] = 0 

    cartella_dict = {"id": id, "cartella": righe}
    return cartella_dict

def estrai_numero(numeri_estratti: list[int])->int:
    while len(numeri_estratti)<90:
        numero=random.randint(1,90)
        if numero not in numeri_estratti:
            numeri_estratti.append(numero)
            return numero
    return 0


def controlla_cartella(cartella: dict, numeri_estratti:list[int])->list[bool]:
    conta=[0,0,0]
    for riga in range(3):
        for colonna in range(9):
            if cartella["cartella"][riga][colonna] in numeri_estratti:
                conta[riga]+=1
    
    if sum(conta)==15:
        return [True,True,True,True,True]
    elif max(conta)==5:
        return [True,True,True,True,False]
    elif max(conta)==4:
        return [True,True,True,False,False]
    elif max(conta)==3:
        return [True,True,False,False,False]
    elif max(conta)==2:
        return [True,False,False,False,False]
    else:
        return [False,False,False,False,False]



cartelle=[]
for i in range(4):  
    cartelle.append(genera_cartella(i))
    print(cartelle[i])


numeri_estratti=[]
stato_estrazione=0
vincite=["ambo","terno","quaterna", "cinquina","tombola"]

estratto=estrai_numero(numeri_estratti)
while estratto!=0:
    print(estratto)
    incrementa_stato=False
    for cartella in cartelle:
        controllo=controlla_cartella(cartella,numeri_estratti)
        if controllo[stato_estrazione]:
            print(f"la cartella con id = {cartella['id']} ha fatto {vincite[stato_estrazione]}")
            incrementa_stato=True
    if incrementa_stato:
        stato_estrazione+=1
        
    if stato_estrazione==5:
        break
    else:
        input("Premi invio per estrarre...")
        estratto=estrai_numero(numeri_estratti)
