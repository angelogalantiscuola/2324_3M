nome = str(input("Inserire nome:"))
fotocopie = int(input("Inserire il numero di copie: "))
plico_input = str(input("aggiungere plico?(Y/N) "))
plico = 1.80
if fotocopie >= 1 and fotocopie <= 19:
    if plico_input == "y" or plico_input == "Y":
        costo1 = fotocopie * 0.10
        print(f"Gentile Sig. {nome} il suo preventivo è di {costo1 + plico} euro compresa la rilegatura")
    elif plico_input == "n" or plico_input == "N":
        costo1 = fotocopie * 0.10
        print(f"Gentile Sig. {nome} il suo preventivo è di {costo1} euro")
elif fotocopie >= 20 and fotocopie <= 100:
    if plico_input == "y" or plico_input == "Y":
        costo2 = fotocopie * 0.10
        print(f"Gentile Sig. {nome} il suo preventivo è di {costo2 + plico} euro compresa la rilegatura")
    elif plico_input == "n" or plico_input == "N":
        costo2 = fotocopie * 0.10
        print(f"Gentile Sig. {nome} il suo preventivo è di {costo2} euro")
elif fotocopie > 100:
    if plico_input == "y" or plico_input == "Y":
        costo3 = fotocopie * 0.05
        print(f"Gentile Sig. {nome} il suo preventivo è di {costo3 + plico} euro compresa la rilegatura")
    elif plico_input == "n" or plico_input == "N":
        costo3 = fotocopie * 0.10
        print(f"Gentile Sig. {nome} il suo preventivo è di {costo3} euro")
else:
    print("!!ERRORE!!")
