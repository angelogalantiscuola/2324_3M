# In una copisteria, il costo unitario delle fotocopie varia a seconda del numero da effettuare secondo la seguente tabella:
# n.1-19 0,10 euro, n.20-100 0,08 euro, piu di 100 0,05 euro. 
# Inoltre se le fotocopie sono da rilegare viene aggiunto un costo di 1,80 euro.
# Dati in input il numero di fotocopie da effettuare, il nome del cliente e un indicazione che segnali se il plico è da rilegare, calcola il costo totale e stampa il seguente prospetto:
# Gentile Sig. ___ il suo preventivo è di ___ euro compresa la rilegatura. L'ultima riga è da scrivere solo se è richiesta la rilegatura

numero_fotocopie = int(input("Inserisci il numero di fotocopie:"))
nome_cliente = input("Inserisci il nome del cliente:")
copie_da_rilegare = input("le copie sono da rilegare(S/N):")

if numero_fotocopie >= 1 and numero_fotocopie <= 19:
    costo_per_fotocopia = 0.10
elif numero_fotocopie >= 20 and numero_fotocopie <= 100:
    costo_per_fotocopia = 0.08
else:
    costo_per_fotocopia = 0.05

costo_totale = numero_fotocopie * costo_per_fotocopia
if copie_da_rilegare == "S":
    costo_totale += 1.80 
    print (f"Gentile sig. {nome_cliente} il suo preventivo è di {costo_totale} euro compresa la rilegatura.")
elif copie_da_rilegare == "N":
    print(f"Gentile sig {nome_cliente} il suo preventivo è di {costo_totale} euro.")






