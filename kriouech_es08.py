numero_pasticcini = int(input("Inserisci il numero di pasticcini:"))

scatole5 = numero_pasticcini // 5
resto5 = numero_pasticcini % 5

scatole3 = resto5 // 3
resto3 = resto5 % 3 

scatole1 = resto3

print("Scatole da 5 pezzi",scatole5)
print("Scatole da 3 pezzi",scatole3)
print("Scatole da 1 pezzo",scatole1)