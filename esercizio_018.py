#Esercizio 18
#Scrivere un programma che passati in input n valori popoli una lista.
#In seguito scorre lista con un for e ne calcola il valore medio, il massimo e il minimo.
n_valori = int(input("numero valori"))
list=[]
media=0
for i in range(n_valori):
    list.append(i)
print(list)
for o in range(n_valori):
    media+=list[o]
media=media/n_valori
print(f"media {media}") 
minimo=list[0]   
massimo=list[-1]
print(f"minimo{minimo}")
print(f"massimo{massimo}")