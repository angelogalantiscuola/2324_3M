# pyright: basic
"""
Handle the catalog of a museum.
(not complete)
"""


import sys  # modulo system: permette di usare sys.exit() per uscire dal programma


opera1 = {"titolo": "la gioconda", "artista": "leonardo", "anno": 1500}
opera2 = {"titolo": "la nascita di venere", "artista": "botticelli", "anno": 1500}
opera3 = {"titolo": "la primavera", "artista": "botticelli", "anno": 1500}
stanza1 = {"id": 1, "denominazione": "impressionisti", "metratura": 20, "opere": [opera1, opera2]}
stanza2 = {"id": 2, "denominazione": "impressionisti", "metratura": 20, "opere": [opera3]}

stanza3 = {  # type: ignore
    "id": 3,
    "denominazione": "stanza vuota",
    "metratura": 20,
    "opere": [],
}
museo = [stanza1, stanza2, stanza3]  # type: ignore


if False:
    # Consultare le opere presenti in una stanza
    # id_stanza_da_consultare = int(input("inserisci id della stanza"))
    ID_STANZA_DA_CONSULTARE = 1
    # trova la stanza con id pari a id_stanza_da_consultare
    stanza_da_consultare = {}
    for stanza in museo:  # type: ignore
        if stanza["id"] == ID_STANZA_DA_CONSULTARE:
            stanza_da_consultare = stanza  # type: ignore
    if not stanza_da_consultare:
        print("Stanza non trovata")
        sys.exit()
    print(f"Stanza da consultare: {stanza_da_consultare}")
    # stampa tutte le opere della stanza
    opere_della_stanza = stanza_da_consultare["opere"]
    # print(opere_della_stanza)  # controllo
    # print(type(opere_della_stanza))  # controllo
    for opera in opere_della_stanza:  # type: ignore
        print(f"Titolo: {opera['titolo']}, artista: {opera['artista']}, anno: {opera['anno']}")

    # 4. Consultare le stanze presenti
    for stanza in museo:  # type: ignore
        print(f"id: {stanza['id']}, denominazione: {stanza['denominazione']}, metratura: {stanza['metratura']}")

    # 5. Cercare le informazioni su un opera
    # cercare l'opera a partire dal suo nome in tutte le stanze e poi stampare le informazioni
    OPERA_DA_CERCARE = "la primavera"
    opera_presente = False  # pylint: disable=invalid-name
    for stanza in museo:  # type: ignore
        opere_della_stanza = stanza["opere"]
        for opera in opere_della_stanza:  # type: ignore
            if opera["titolo"] == OPERA_DA_CERCARE:
                opera_presente = True  # pylint: disable=invalid-name
                print("Opera trovata")
                print(f"Titolo: {opera['titolo']}, artista: {opera['artista']}, anno: {opera['anno']}")
                break
    if opera_presente is False:
        print("Opera non trovata")

    # 7. Cancellare una stanza solo se vuota
    STANZA_DA_CANCELLARE = 3
    stanza_trovata = False
    for stanza in museo:  # type: ignore
        if stanza["id"] == STANZA_DA_CANCELLARE:
            stanza_trovata = True
            if stanza["opere"] != []:
                print("La stanza non è vuota")
            else:
                museo.remove(stanza)
                print("Stanza rimossa")

    # 6. Cancellare un opera
    OPERA_DA_CANCELLARE = "la primavera"
    opera_presente = False  # pylint: disable=invalid-name
    for stanza in museo:  # type: ignore
        opere_della_stanza = stanza["opere"]
        for opera in opere_della_stanza:  # type: ignore
            if opera["titolo"] == OPERA_DA_CANCELLARE:
                opera_presente = True  # pylint: disable=invalid-name
                print("Opera trovata")
                opere_della_stanza.remove(opera)  # type: ignore
                break
    if opera_presente is False:
        print("Opera non trovata")


# 2. Aggiungere un opera ad una stanza(titolo, artista, anno)
ID_STANZA = 1
OPERA_TITOLO = "La notte stellata"
OPERA_ARTISTA = "Van Gogh"
OPERA_ANNO = 1800
OPERA_DA_AGGIUNGERE = {"titolo": OPERA_TITOLO, "artista": OPERA_ARTISTA, "anno": OPERA_ANNO}
stanza_trovata = False  # assegnazione
for stanza in museo:
    if stanza["id"] == ID_STANZA:
        # stanza trovata
        stanza_trovata = True  # assegnazione
        stanza["opere"].append(OPERA_DA_AGGIUNGERE)
if stanza_trovata is False:  # controllo
    print("Stanza non trovata, non è stato possibile aggiungere l'opera")

# 1. Creare una nuova stanza (id, denominazione, metratura)
STANZA_ID = 4
STANZA_DENOMINAZIONE = "cubismo"
STANZA_METRATURA = 40
STANZA_DA_AGGIUNGERE = {
    "id": STANZA_ID,
    "denominazione": STANZA_DENOMINAZIONE,
    "metratura": STANZA_METRATURA,
    "opere": [],
}
museo.append(STANZA_DA_AGGIUNGERE)
