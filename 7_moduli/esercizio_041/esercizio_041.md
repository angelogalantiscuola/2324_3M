# Gestione di un sistema di prenotazione per un cinema

Scrivi un programma che gestisce un sistema di prenotazione per un cinema. Il cinema ha diverse sale, ognuna con un numero diverso di posti. Gli utenti possono prenotare posti per uno specifico film in una specifica sala. Il programma deve permettere all'utente di:

- Aggiungere una sala al cinema.
- Rimuovere una sala dal cinema.
- Visualizzare tutte le sale del cinema.
- Aggiungere un film a una sala.
- Rimuovere un film da una sala.
- Visualizzare tutti i film in una sala.
- Prenotare un posto per un film in una sala.
- Annullare una prenotazione per un film in una sala.

In questo esercizio, il cinema è rappresentato come un dizionario di tipo Cinema, dove ogni chiave è il nome di una sala e il valore è un altro dizionario di tipo Sala che contiene i dettagli della sala, come il numero di posti disponibili e l'elenco dei film in programmazione. Le funzioni modificano e interagiscono con questo dizionario per gestire il cinema.