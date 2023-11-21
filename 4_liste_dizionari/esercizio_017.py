my_list=[]
numero_valori=int(input('quanti valori vuoi inserire nella lista?  '))
for valore in range(numero_valori):
    my_list.append(valore)
se_valore=int(input('verifica il valore: '))
if se_valore in my_list:
    print('presente')
else:
    print('non presente')