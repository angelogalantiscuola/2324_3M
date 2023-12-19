#Inizializza una lista di dizionari, ognuno rappresentante un dipendente con nome, ruolo e stipendio iniziale.
dipendenti = [
    {"nome": "Mario", "ruolo": "commerciale", "stipendio": 1000},
    {"nome": "Luigi", "ruolo": "amministrativo", "stipendio": 2000},
    {"nome": "Giovanni", "ruolo": "programmatore", "stipendio": 3000},
]

# Inizializza una lista di progetti con un budget iniziale e costo orario.
progetti = [
    {"nome": "next_google", "budget": 10000, "costo_orario": 100},
    {"nome": "amazon_but_better", "budget": 20000, "costo_orario": 200},
]

# Assegna a ciascun dipendente un impegno in ore su questo nuovo progetto, 
# sottraendo dal budget del progetto il costo dei dipendenti per le ore svolte 
# e sommando allo stipendio iniziale i compensi accessori per i progetti 
# su cui ha lavorato.
ore_lavorate_per_progetto = [
    {"nome_progetto": "next_google", "nome_dipendente": "Mario", "ore": 10},
    {"nome_progetto": "next_google", "nome_dipendente": "Luigi", "ore": 20},
    {"nome_progetto": "amazon_but_better", "nome_dipendente": "Giovanni", "ore": 30},
]

# stampa le ore lavorate per progetto per ogni dipendente
for ore_lavorate in ore_lavorate_per_progetto:
    print(f"Nome progetto: {ore_lavorate['nome_progetto']}, Nome dipendente: {ore_lavorate['nome_dipendente']}, Ore: {ore_lavorate['ore']}")