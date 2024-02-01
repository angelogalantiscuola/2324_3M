#Esercizio 29

# Scrivi una funzione che ricevuta in ingresso una lista di dizionari contenenti le fatture di n utenti così formate:
#{"id":"id_utente",
#"importo":128.54,
#"sconto_fattura":15}
#svolga le seguenti funzioni:
#1) Aggiunga ad ogni dizionario una nuova chiave "importo_scontato" al quale associa il valore dell'importo scontato in base alla percentuale indicata alla chiave "sconto_fattura";
#2) Restituisca una lista di float dove il primo elemento è il totale degli importi e il secondo il totale degli importi scontati;
#3) Restituisca None se la lista delle fatture è vuota.

#La funzione ha la seguente signature:
#def calcola_importo(fatture:list[dict])->list[float]|None: ...... 

#Si provi la funzione in un programma dove le si dia in ingresso la seguente lista:
#fatture=[
#{"id":"Monticelli",
#"importo":245.78,
#"sconto_fattura":10
#},
#{"id":"Kola",
#"importo":325.71,
#"sconto_fattura":12
#},
#{"id":"Romagna",
#"importo":245.78,
#"sconto_fattura":8
#},
#{"id":"Bilancioni",
#"importo":245.78,
#"sconto_fattura":15
#},
#{"id":"Sanchi",
#"importo":245.78,
#"sconto_fattura":5
#},
#{"id":"Pontellini",
#"importo":245.78,
#"sconto_fattura":18
#},
#{"id":"Clementi",
#"importo":245.78,
#"sconto_fattura":20
#},
#{"id":"Arlotti",
#"importo":245.78,
#"sconto_fattura":19
#},
#{"id":"Nedria",
#"importo":245.78,
#"sconto_fattura":7
#},
#{"id":"Santini",
#"importo":245.78,
#"sconto_fattura":22
#},
#]

def creazione_nuova_fattura () -> list | None:

    fatture = []

    numero = int (input ("Quante fatture vuoi creare?"))
    
    if numero == 0:
        return None
    
    elif numero != 0:

        for x in range (numero):

            user = {"id": None,
                    "sconto": None,
                    "sconto in fattura": None
                    }

            id = str (input ("Inserisci il tuo id: "))
            quantità = float (input ("Inserisci la quantità della tua fattura: "))
            sconto_fattura = int (input ("Inserisci lo sconto della tua fattura: "))

            quantità_scontata = (quantità * (100 - sconto_fattura)) / 100

            user.update ({"id": id, "quantità": quantità, "sconto fattura": sconto_fattura, "quantità scontata": quantità_scontata})
            fatture.append (user)

            print (f"{user}")

        return fatture
    
    else: print ("Errore")

def calcolo_dellimporto_dello_sconto (fatture: list [dict]) -> list [float] | None:

    if fatture == []:
        return None
    
    elif fatture != []:

        quantità_totale = 0
        importo_totale_dello_sconto = 0

        for fattura in fatture:

            quantità_totale += fattura ["quantità"]
            importo_totale_dello_sconto += fattura ["quantità scontata"]

        print (f"Le quantità totali sono: {quantità_totale}.\nLe quantità totali scontate sono: {importo_totale_dello_sconto}")
    
    else: print ("Errore")

fatture = creazione_nuova_fattura ()
calcolo_dellimporto_dello_sconto (fatture)