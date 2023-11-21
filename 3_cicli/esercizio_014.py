#Scrivi un programma che calcoli il valore della circonferenza e quello dell'area di tutti i cerchi con raggio compreso tra 1 e 20.

import math

for raggio in range(1, 21):
    circonferenza = 2 * math.pi * raggio
    area = math.pi * raggio**2
    print(f"Raggio: {raggio}, Circonferenza: {circonferenza}, Area: {area}")