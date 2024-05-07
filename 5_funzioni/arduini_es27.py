
def input_i() -> list[int]: 
    i = int(input("Inserisci il numero di valori da inserire: "))
    return [int(input("Inserisci un valore: ")) for i in range(i)]
def is_pari(num: int) -> bool:
    return num % 2 == 0
def somma_quadrati(lista_valori: list[int]) -> int:
    return sum(valore ** 2 for valore in lista_valori if is_pari(valore))
valori_inseriti = input_i()
print(f"Valori inseriti: {valori_inseriti}")
numero_da_verificare = int(input("Inserisci un numero da verificare se è pari: "))
risultato_is_pari = is_pari(numero_da_verificare)
print(f"Il numero {numero_da_verificare} è pari? {risultato_is_pari}")
risultato_somma_quadrati = somma_quadrati(valori_inseriti)
print(f"La somma dei quadrati dei numeri pari nella lista è: {risultato_somma_quadrati}")




