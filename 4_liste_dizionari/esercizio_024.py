
"""
Immagina di dover gestire le risorse umane e finanziarie di un'azienda con dipendenti e progetti. Crea un programma che:

Inizializza una lista di dizionari, ognuno rappresentante un dipendente con nome, ruolo e stipendio iniziale.
Stampa la lista di dipendenti.
Aggiungi un nuovo progetto alla tua azienda con un budget iniziale e costo orario per ora di lavoro su di esso.
Assegna a ciascun dipendente un impegno in ore su questo nuovo progetto, sottraendo dal budget del progetto il costo dei dipendenti per le ore svolte e sommando allo stipendio iniziale i compensi accessori per i progetti su cui ha lavorato.
Stampa la lista dei dipendenti con i relativi stipendi totali e le ore lavorate per ciascun progetto.
Stampa le ore lavorate totali e il budget rimanente per ogni progetto.
"""


while True:
    Scelta = (input("Inserire un input: "))
    match Scelta:
        case "1":
            Azienda = []
            Progetti = []

            Nome_Lavoratore = str(input("Inserisci nome lavoratore: "))
            Ruolo_Lavoratore = str(input("Inserisci ruolo lavoratore: "))
            Stipendio_Lavoratore = int(input("Inserisci stipendio lavoratore: "))
            Ore_totali = int(input("Inserisci ore totali: "))
            aggiungi_lavoratore = {"Nome": Nome_Lavoratore, "denominazione": Ruolo_Lavoratore, "Stipendio": Stipendio_Lavoratore,"Ore totali": Ore_totali}
            Azienda.append(aggiungi_lavoratore)

        case "2":

         print(Azienda)


        case "3":

            Progetto_nome = (input("Inserisci nome del progetto: "))
            Progetto_Budget = int((input("Inserisci budget del progetto: ")))
            Progetto_Costo_Ora = int((input("Inserisci costo all'ora del progetto: ")))
            Aggiungi_Progetto = {"Nome": Progetto_nome, "Budget": Progetto_Budget, "Costo all'ora": Progetto_Costo_Ora, "Dipendenti": []}
            Progetti.append(Aggiungi_Progetto)

        case "4":

         Assegna_lavoratore = (input("Inserisci lavoratore da assegnare : "))
         Assegna_Progetto = (input("Inserisci progetto per assegnare il lavoratore : "))
         for Lavoratori in Azienda:
                if Lavoratori["Nome"] == Assegna_lavoratore:
                 print("Lavoratore localizzato lmao")
                else:
                        break    

                for Project in Progetti:
                    if Project["Nome"] == Assegna_Progetto:
                        Project["Dipendenti"].append(Assegna_lavoratore)
                    else:
                     break


        case "5":
         Assegna_ore = int(input("Inserisci ore del lavoratore: "))
         Lavoratore_nome = str(input("Inserisci nome lavoratore: "))
         Progetto_nome = input("Inserisci nome progetto: ")
         for lavoratori in Progetti:
                 if lavoratori["Dipendenti"] == Lavoratore_nome:
                    lavoratori["Ore totali"] = Assegna_ore + lavoratori["Ore totali"]
                    print (lavoratori["Ore totali"])

                 for Project in Progetti:
                  if Project["Nome"] == Progetto_nome:
                   Soldi = Project["Costo all'ora"] * Assegna_ore
                   Project["Budget"] = Project["Budget"] - Soldi

                 for lavoratori in Azienda:
                      if lavoratori["Nome"] == Lavoratore_nome:
                        lavoratori["Stipendio"] = lavoratori["Stipendio"] + Soldi


        case "6":
         print(Azienda)



        case "7":
         print(Progetti)

        case "8":
         break


