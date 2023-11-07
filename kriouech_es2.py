num_giorni = int(input("Inserisci il numero di giorni: "))
num_ombrelloni = int(input("Inserisci il numero di ombrelloni desiderati: "))
num_lettini = int(input("Inserisci il numero di lettini desiderati: "))
num_sedie = int(input("Inserisci il numero di sedie a sdraio desiderate: "))

costo_ombrelloni = 12 * num_ombrelloni
costo_lettini = 5 * num_lettini
costo_sedie = 6.50 * num_sedie
spesa_totale = (costo_ombrelloni + costo_lettini + costo_sedie) * num_giorni

print("La spesa complessiva è di", spesa_totale, "euro.")
