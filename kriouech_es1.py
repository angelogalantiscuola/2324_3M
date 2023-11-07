ombrellone = int(12)
lettini = int(5)
sdraio = float(6.50)

ombrellone1 = int(input("Inserisci il numero di ombrelloni:"))
lettini1 = int(input("Inserisci il numero di lettini:"))
sdraio1 = int(input("Inserisci il numero di sdraio:"))

costo =  (ombrellone*ombrellone1+lettini*lettini1+sdraio*sdraio1)*giorni
giorni = int(input("Inserisci il numero dei giorni:"))
servizi = (input("Inserisci il servizio richiesto:"))

print("La spesa complessiva è:", costo)
