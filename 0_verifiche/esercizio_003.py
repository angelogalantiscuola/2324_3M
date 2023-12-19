settimana = {'lunedi':['studio'],
              'martedi':['studio'],
              'mercoledi':['studio'],
              'giovedi':['studio','palestra'],
              'venerdi':['studio'],
              'sabato':['studio'],
              'domenica':['studio']}
for giorno,lista_attivita in settimana.items():
    print(f'{giorno}:') 
    for attivita in lista_attivita:
        print(f'\t{attivita}')

settimana['sabato'].append('palestra')

for giorno,lista_attivita in settimana.items():
    print(f'{giorno}:') 
    for attivita in lista_attivita:
        print(f'\t{attivita}')


