#ESERCIZIO 23:liste di dizionari: imparare a combinare il precedente argomento (le liste) con i dizionari.
#Realizzare un applicativo che permetta, mediante l'uso di dizionari e liste, la gestione del catalogo di un museo.
#In particolare, l'applicativo dovrà permettere di:
#1) Creare una nuova stanza (id, denominazione, metratura) 
#2) Aggiungere un opera ad una stanza(titolo, artista, anno)
#3) Consultare le opere presenti in una stanza
#4) Consultare le stanze presenti
#5) Cercare le informazioni su un opera
#6) Cancellare un opera
#7) Cancellare una stanza solo se vuota
#NB 
#- Progettare la struttura dati a priori in modo da garantire le funzionalità richieste.
#- Fare in modo che il museo sia inizialmente vuoto e popolabile da applicativo.
#- Realizzare un menù numerato con le varie funzionalità elencate in precedenza.
#- Controllare la presenza della stanza e/o dell'opera prima di aggiungerla.

stanze={'1':['picasso',100]}
opere=[]

def printmenu(lx):
    print()
    print("Scegliere l'opzione desiderata") 
    for item in lx:
        print(item)

lm= ['1) Visualizza stanze', '2) Aggiunge opera a stanza', \
     '3) consulta le opere in una stanza','4) Consulta le stanze presenti',\
     '5) cerca informazioni su una opera','6) cancella opera',\
     '7) cancella stanza se vuota','8) esci']

printmenu(lm)

def vediStanze(stanze):
    print()
    print("visualizza stanze")

    for item in stanze:
        print('id=',item,stanze[item][0],stanze[item][1]) 

def aggStanza(stanze):
    idx=input('identificativo')
    nome=input('nome stanza')
    area=input('metratura')
    stanze[idx]=[nome,area]
    return stanze

def aggiungi(opere):
    ids=input('identificativo stanza:')
    titolo=input('titolo:',)
    artista=input('artista:')
    anno=input('anno:')
    opere.append([ids,titolo,artista,anno])
    return opere

def visualizzaOpere(opere):
    print()
    for item in opere:
        print(item)

def consulta(opere):
    print()
    vediStanze(stanze)
    ids=input('stanza scelta:')
    for item in opere:
        if ids==item[0]:
            print('titolo:',item[1],'artista:',item[2],'anno:',item[3])
       
             

s=0
while s !=8:
    s=input("scelta:")
    s=int(s)
    if s ==1:
        vediStanze(stanze)
        stanze=aggStanza(stanze)
        vediStanze(stanze)
        printmenu(lm)
    elif s==2:
        vediStanze(stanze)
        opere=aggiungi(opere)
        print(opere)
        visualizzaOpere(opere)
        printmenu(lm)
    elif s ==3:
        consulta(opere)
        printmenu(lm)
    elif s ==4:
        vediStanze(stanze)
        printmenu(lm)
    elif s ==5:
        visualizzaOpere(opere)
        opera=input('opera scelta:')
        for item in opere:
            if opera==item[1]:
                print('artista:',item[2],' anno:',item[3])
                break
        printmenu(lm)
    elif s ==6:
        visualizzaOpere(opere)
        opera=input('opera scelta:')
        i=0
        for item in opere:
            print('item',item)
            if opera==item[1]:
                print('artista:',item[2],' anno:',item[3])
                opere.pop(i)
                break
            i=i+1
        printmenu(lm)
    elif s ==7:
        vediStanze(stanze)
        ids=input('stanza da eliminare:')
        vuota=True
        for item in opere:
            if ids==item[0]:
                vuota=False
                break
        if vuota==True:
            del stanze[ids]
        vediStanze(stanze)
        printmenu(lm)
        
             
            
print("programma terminato")