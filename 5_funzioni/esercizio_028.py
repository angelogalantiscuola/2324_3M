"""
Scrivere una funzione che passati come parametro la classe ambientale (euro 0, euro1,...., euro6), i kW e gli anni passati dall'immatricolazione di un autoveicolo,
calcoli il bollo auto e l'eventuale superbollo. Nel caso non sia previsto il superbollo si scelga se restituire 0 oppure None. Utilizzare la funzione in un programma
di esempio.

N.B.
Creare una funzione specifica per il superbollo da usare nella funzione principale.
es.
def calcola_superbollo (kW:int, immatricolazione: int) ->float: ....

Signature metodo principale:
def calcola_bollo (classe_ambientale:int, kW:int, immatricolazione:int) ->list[float] | None: ....
N.B.
La funzione può eseguire un controllo sui dati inseriti in ingresso e in caso di dati non validi (es. negativi) restituisce None


utilizzo:
bollo, superbollo = calcola_bollo (.......................................

Calcolo bollo:
Euro 0 fino a 100 kW pagano 3 euro a kW e 4,50 euro per ogni kW oltre i 100
Euro 1 fino a 100 kW pagano 2,9 euro a kW e 4,35 euro per ogni kW oltre i 100
Euro 2 fino a 100 kW pagano 2,8 euro a kW e 4,20 euro per ogni kW oltre i 100
Euro 3 fino a 100 kW pagano 2,7 euro a kW e 4,05 euro per ogni kW oltre i 100
Euro 4 fino a 100 kW pagano 2,58 euro a kW e 3,87 euro per ogni kW oltre i 100
Euro 5 fino a 100 kW pagano 2,58 euro a kW e 3,87 euro per ogni kW oltre i 100
Euro 6 fino a 100 kW pagano 2,58 euro a kW e 3,87 euro per ogni kW oltre i 100
Calcolo superbollo:
Auto nuove e fino a 5 anni pagano 20 euro per ogni kW oltre i 185
Dopo i primi 5 anni pagano 12 euro per ogni kW oltre i 185
Dopo i 10 anni pagano 6 euro per ogni kW oltre i 185
Dopo i 15 anni pagano 3 euro per ogni kW oltre i 185
Dopo i 20 anni non pagano il superbollo
"""


def input_auto() -> list[str]: #input dei dati necessari per i calcoli
    kilowat = float(input("inserire i kilowat della auto\n\n"))
    classe = int(input("inserire la classe della auto\n\n"))
    età = int(input("inserire l'età dell'auto\n\n"))
    return kilowat,classe,età


def superbollo(kilowat,età) -> int | None:    #calcolo superbollo
    ris_kw2 = 0    
    if kilowat > 185:

        if età <= 5 :
                kilowat = kilowat - 185
                ris_kw2 = kilowat * 12
        elif 10 > età > 5:
            kilowat = kilowat - 185
            ris_kw2 = kilowat * 6

        elif 10 < età < 15:
            kilowat = kilowat - 185
            ris_kw2 = kilowat * 6

        elif 15 < età <= 20:
            kilowat = kilowat - 185
            ris_kw2 = kilowat * 6

        elif età > 20:
            ris_kw2 = 0

    return ris_kw2


def bollo(kilowat,classe) -> float | None:  #calcolo bollo

    if classe == 0 and kilowat <= 100:
        ris_kw = kilowat*3
    elif classe == 0 and kilowat > 100:
        resto = kilowat - 100
        momentaneo = 100 * 3 #calcolo della parte dei 100 kw non superati
        ris_kw = resto * 4.50
        ris_kw = ris_kw + momentaneo


    elif classe == 1 and kilowat <= 100:
        ris_kw = kilowat*2.9
    elif classe == 1 and kilowat > 100:
        resto = kilowat - 100
        momentaneo = 100 * 2.9 #calcolo della parte dei 100 kw non superati
        ris_kw = resto * 4.35
        ris_kw = ris_kw + momentaneo


    elif classe == 2 and kilowat <= 100:
        ris_kw = kilowat*2.8
    elif classe == 2 and kilowat > 100:
        resto = kilowat - 100
        momentaneo = 100 * 2.8 #calcolo della parte dei 100 kw non superati
        ris_kw = resto * 4.20
        ris_kw = ris_kw + momentaneo
    

    elif classe == 3 and kilowat <= 100:
        ris_kw = kilowat*2.70
    elif classe == 3 and kilowat > 100:
        resto = kilowat - 100
        momentaneo = 100 * 2.70 #calcolo della parte dei 100 kw non superati
        ris_kw = resto * 4.05
        ris_kw = ris_kw + momentaneo


    elif classe == 4 or classe == 5 or classe == 6 and kilowat <= 100:
        ris_kw = kilowat*2.58
    elif classe == 4 or classe == 5 or classe == 6 and kilowat > 100:
        resto = kilowat - 100
        momentaneo = 100 * 2.58 #calcolo della parte dei 100 kw non superati
        ris_kw = resto * 3.87
        ris_kw = ris_kw + momentaneo
    elif classe <0 or classe>6:
        ris_kw = None
    return ris_kw

kilowat,classe,età = input_auto()

ris_kw = bollo(kilowat,classe)
ris_kw2 = superbollo(kilowat,età)

if not ris_kw == None:
    print(f"con la tua classe energetica di {classe} ti tocca pagare {ris_kw} EURO per il bollo,\nti tocca pagare {ris_kw2} EURO per il super bollo")
else:
    print("(ERRROR) si ha inserito un valore di classe energetica sbagliata")

