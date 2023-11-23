"""
Handle the catalog of a museum.
(not complete)
(testing type hinting)
"""

import sys
from typing import Dict, Union, List


OperaType = Dict[str, Union[str, int]]
StanzaType = Dict[str, Union[str, int, List[OperaType]]]
MuseoType = List[StanzaType]

opera1: OperaType = {"titolo": "la gioconda", "artista": "leonardo", "anno": 1500}
opera2: OperaType = {"titolo": "la nascita di venere", "artista": "botticelli", "anno": 1500}
opera3: OperaType = {"titolo": "la primavera", "artista": "botticelli", "anno": 1500}
stanza1: StanzaType = {
    "id": 1,
    "denominazione": "impressionisti",
    "metratura": 20,
    "opere": [opera1, opera2],
}
stanza2: StanzaType = {
    "id": 2,
    "denominazione": "impressionisti",
    "metratura": 20,
    "opere": [opera3],
}
museo: MuseoType = [stanza1, stanza2]

# Consultare le opere presenti in una stanza
# id_stanza_da_consultare = int(input("inserisci id della stanza"))
ID_STANZA_DA_CONSULTARE = 1
# trova la stanza con id pari a id_stanza_da_consultare
stanza_da_consultare: StanzaType = {}
for stanza in museo:
    if stanza["id"] == ID_STANZA_DA_CONSULTARE:
        stanza_da_consultare = stanza
if not stanza_da_consultare:
    print("Stanza non trovata")
    sys.exit()
print(f"Stanza da consultare: {stanza_da_consultare}")
# stampa tutte le opere della stanza
opere_della_stanza: List[OperaType] = stanza_da_consultare["opere"]
print(opere_della_stanza)
print(type(opere_della_stanza))
for opera in opere_della_stanza:
    print(f"Titolo: {opera['titolo']}, artista: {opera['artista']}, anno: {opera['anno']}")


# 4. Consultare le stanze presenti
for stanza in museo:
    print(f"id: {stanza['id']}, denominazione: {stanza['denominazione']}, metratura: {stanza['metratura']}")


# 5. Cercare le informazioni su un opera
# cercare l'opera a partire dal suo nome in tutte le stanze e poi stampare le informazioni
OPERA_DA_CERCARE = "la primavera"
opera_presente = False # pylint: disable=invalid-name
for stanza in museo:
    opere_della_stanza = stanza["opere"]
    for opera in opere_della_stanza:
        if opera["titolo"] == OPERA_DA_CERCARE:
            opera_presente = True # pylint: disable=invalid-name
            print("Opera trovata")
            print(f"Titolo: {opera['titolo']}, artista: {opera['artista']}, anno: {opera['anno']}")
            break
if opera_presente is False:
    print("Opera non trovata")

# 2. Aggiungere un opera ad una stanza(titolo, artista, anno)
ID_STANZA = 1
OPERA_TITOLO = "La notte stellata"
OPERA_ARTISTA = "Van Gogh"
OPERA_ANNO = 1800
OPERA_DA_AGGIUNGERE = {"titolo": OPERA_TITOLO, "artista": OPERA_ARTISTA, "anno": OPERA_ANNO}
for stanza in museo:
    if stanza["id"] == ID_STANZA:
        # stanza trovata
        stanza["opere"].append(OPERA_DA_AGGIUNGERE)


# stampa tutte le opere della stanza
opere_della_stanza = stanza1["opere"]
for opera in opere_della_stanza:
    print(f"Titolo: {opera['titolo']}, artista: {opera['artista']}, anno: {opera['anno']}")
