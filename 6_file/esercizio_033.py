# Scrivere una programma che letto da file JSON una lista di dizionari contenenti le fatture di n utenti così formate:
# {"id":"id_utente",
# "importo":128.54,
# "sconto_fattura":15}
# svolga le seguenti funzioni:
# 1) Mostri tutte le fatture

# importare il modulo json
import json


def leggi_file_json_come_lista(nome_file: str) -> list:
    # lettura da file JSON
    with open(file=nome_file, mode="r") as file_json:
        try:
            mylist = json.load(file_json)
        except:
            mylist = []
    return mylist


def scrivi_file_json_da_lista(nome_file: str, lista: list) -> None:
    # Scrittura sul file del contenuto aggiornato
    with open(nome_file, "w") as file_json:
        json.dump(obj=lista, fp=file_json, indent=4)


def mostra_fatture(lista: list) -> None:
    for fattura in lista:
        print(fattura)


def aggiungi_fattura(fatture: list, nome_file: str) -> list:
    fattura_da_aggiungere = {"id": "Quattrocchi", "importo": 128.54, "sconto_fattura": 15}
    fatture.append(fattura_da_aggiungere)
    # TODO possiamo inserire in append solo
    # l'ultima fattura nel file invece di riscrivere tutto
    scrivi_file_json_da_lista(nome_file, fatture)
    return fatture


def aggiungi_importo_scontato(fatture: list, idx: int) -> list:
    fatture[idx]["importo_scontato"] = fatture[idx]["importo"] - (
        fatture[idx]["importo"] * fatture[idx]["sconto_fattura"] / 100
    )
    return fatture


def main():  # principale
    nome_file = "esercizio_033.json"
    fatture = leggi_file_json_come_lista(nome_file)
    mostra_fatture(fatture)
    fatture = aggiungi_fattura(fatture, nome_file)
    fatture = aggiungi_importo_scontato(fatture, 0)
    scrivi_file_json_da_lista(nome_file, fatture)


if __name__ == "__main__":
    main()
