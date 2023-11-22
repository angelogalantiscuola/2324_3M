"""
Handle the catalog of a museum.
(not complete)
"""
# import sys

opera1 = {"titolo": "la gioconda", "artista": "leonardo", "anno": 1500}
opera2 = {"titolo": "la nascita di venere", "artista": "botticelli", "anno": 1500}
opera3 = {"titolo": "la primavera", "artista": "botticelli", "anno": 1500}
stanza1 = {
    "id": 1,
    "denominazione": "impressionisti",
    "metratura": 20,
    "opere": [opera1, opera2],
}
stanza2 = {
    "id": 2,
    "denominazione": "impressionisti",
    "metratura": 20,
    "opere": [opera3],
}
museo = [stanza1, stanza2]

# # Consultare le opere presenti in una stanza
# # id_stanza_da_consultare = int(input("inserisci id della stanza"))
# ID_STANZA_DA_CONSULTARE = 1
# # trova la stanza con id pari a id_stanza_da_consultare
# stanza_da_consultare = {}
# for stanza in museo:
#     if stanza["id"] == ID_STANZA_DA_CONSULTARE:
#         stanza_da_consultare = stanza
# if not stanza_da_consultare:
#     print("Stanza non trovata")
#     sys.exit()
# print(f"Stanza da consultare: {stanza_da_consultare}")
# # stampa tutte le opere della stanza
# opere_della_stanza = stanza_da_consultare["opere"]
# print(opere_della_stanza)
# print(type(opere_della_stanza))
# for opera in opere_della_stanza:  # type: ignore
#     print(f"Titolo: {opera['titolo']}, artista: {opera['artista']}, anno: {opera['anno']}")


# # 4. Consultare le stanze presenti
# for stanza in museo:
#     print(f"id: {stanza['id']}, denominazione: {stanza['denominazione']}, metratura: {stanza['metratura']}")


# # 5. Cercare le informazioni su un opera
# # cercare l'opera a partire dal suo nome in tutte le stanze e poi stampare le informazioni
# OPERA_DA_CERCARE = "la primavera"
# opera_presente = False
# for stanza in museo:
#     for opera in stanza["opere"]:  # type: ignore
#         if opera["titolo"] == OPERA_DA_CERCARE:  # type: ignore
#             opera_presente = True
#             print("Opera trovata")
#             print(f"Titolo: {opera['titolo']}, artista: {opera['artista']}, anno: {opera['anno']}")  # type: ignore
#             break
# if opera_presente == False:
#     print("Opera non trovata")

# 2. Aggiungere un opera ad una stanza(titolo, artista, anno)
ID_STANZA = 1
OPERA_TITOLO = "La notte stellata"
OPERA_ARTISTA = "Van Gogh"
OPERA_ANNO = 1800
OPERA_DA_AGGIUNGERE = {"titolo": OPERA_TITOLO, "artista": OPERA_ARTISTA, "anno": OPERA_ANNO}
for stanza in museo:
    if stanza["id"] == ID_STANZA:
        # stanza trovata
        stanza["opere"].append(OPERA_DA_AGGIUNGERE)  # type: ignore


# stampa tutte le opere della stanza
opere_della_stanza = stanza1["opere"]
for opera in opere_della_stanza:  # type: ignore
    print(f"Titolo: {opera['titolo']}, artista: {opera['artista']}, anno: {opera['anno']}")
