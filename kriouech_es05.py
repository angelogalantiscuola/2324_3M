età = int(input("Inserisci la tua età: "))

if età >= 0 and età <= 12:
    categoria = "bambino"
elif età >= 13 and età <= 19:
    categoria = "adolescente"
elif età >= 20 and età <= 64:
    categoria = "adulto"
else:
    categoria = "anziano"

print("Sei un", categoria)