# Dato in input il numero di secondi dire a quanti anni, mesi, giorni, ore, minuti e secondi corrispondono

secondi = int(input("Inserisci il numero di secondi"))

anni = secondi // (365 * 24 * 60 * 60)
secondi = secondi % (365 * 24 * 60 * 60)

mesi = secondi // (30 * 24 * 60 * 60)
secondi = secondi % (30 * 24 * 60 * 60)

giorni = secondi // (24 * 60 * 60)
secondi = secondi % (24* 60 * 60)

ore = secondi // (60 * 60 )
secondi = secondi % (60 * 60)

minuti = secondi // 60
secondi = secondi % 60

print(anni)
print(mesi)
print(giorni)
print(ore)
print(minuti)
print(secondi)