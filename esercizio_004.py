costoadulto = 10
costominorenne = 6

costoadulto = float(costoadulto)
costominorenne = float(costominorenne)

nadulti = float(input("Inserisci il numero di adulti: "))
nminorenni = float(input("Inserisci il numero di minorenni: "))

costo = (costoadulto * nadulti)+(costominorenne * nminorenni)

print(f"Il costo totale è di {costo}€")