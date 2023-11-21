#2. Dati i seguenti costi giornaliero di un bagnino:
#- ombrellone 12 euro
#- lettini 5 euro
#- sedie a sdraio di 6.50 euro
#Chiedere in input il numero di giorni ed i servizi che vuole prenotare
#Visualizzare la spesa complessiva
giorni = input("inserire giorni di vacanza  ")
giorni = int (giorni)

ombrelloni = input("quanti ombrelloni?   ")#12euro
ombrelloni = int (ombrelloni)
c_ombrelloni = 12


lettini = input("quanti lettini?  ")#5euro
lettini = int (lettini)
c_lettini = 5


sedie = input("quante sedie?    ")#6.50euro
sedie = int (sedie)
c_sedie = 6.50
print(giorni*((ombrelloni*c_ombrelloni)+(lettini*c_lettini)+(sedie*c_sedie)))