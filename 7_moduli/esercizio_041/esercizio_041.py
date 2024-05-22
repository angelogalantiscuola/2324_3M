# In questo esercizio, il cinema è rappresentato come un dizionario
# di tipo Cinema, dove ogni chiave è il nome di una sala e il valore è
# un altro dizionario di tipo Sala che contiene i dettagli della sala,
# come il numero di posti disponibili e l'elenco dei film in programmazione.
# Le funzioni modificano e interagiscono con questo dizionario per gestire
# il cinema.

cinema_mondaino = {
    "Sala_1": {
        "posti": 100,
        "programmazione": ["Il Signore degli Anelli", "Star Wars", "Harry Potter"],
    },
    "Sala_2": {"posti": 50, "programmazione": ["Il Padrino", "Titanic"]},
    "Sala_3": {"posti": 200, "programmazione": ["Il Gladiatore", "Il Re Leone"]},
}


# Aggiungere una sala al cinema.
def aggiungi_sala(cinema: dict, nome_sala: str, posti: int) -> dict:
    cinema[nome_sala] = {"posti": posti, "programmazione": []}
    return cinema


# Rimuovere una sala dal cinema.
def rimuovi_sala(cinema: dict, nome_sala: str) -> dict:
    trovato = False
    for sala in cinema:
        if sala == nome_sala:
            cinema.pop(sala)
            trovato = True
            break
    if not trovato:
        print("Sala non trovata")
    return cinema


if __name__ == "__main__":
    cinema_x = {}
    print(aggiungi_sala(cinema_x, "Sala_4", 150))
    print(rimuovi_sala(cinema_x, "Sala_4"))
    print(rimuovi_sala(cinema_x, "Sala_5"))

# Visualizzare tutte le sale del cinema.
# Aggiungere un film a una sala.
# Rimuovere un film da una sala.
# Visualizzare tutti i film in una sala.
# Prenotare un posto per un film in una sala.
# Annullare una prenotazione per un film in una sala.
