decimale=56

lista_tempo=[]

resto=decimale%2
quoziente=decimale//2
lista_tempo.append(resto)

while quoziente>0:
    resto=quoziente%2
    lista_tempo.append(resto)
    quoziente=quoziente//2
    
    
lista_binaria=[]
i=len(lista_tempo)-1
while i>=0:
    lista_binaria.append(lista_tempo[i])
    i=i-1
    
print(lista_binaria)
    
    