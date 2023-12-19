rubrica = [{
    "nome": "Mario",
    "cognome": "Rossi",
    "telefono": "3331234567"
},{
    'nome': 'Luca',
    'cognome': 'Bianchi',
    'telefono': '3337654321'
},{
    'nome': 'Paolo',
    'cognome': 'Verdi',
    'telefono': '3334567890'
}]
for contatto in rubrica:
    print(contatto['nome'], contatto['cognome'], contatto['telefono'])

rubrica.append({
    'nome': 'Giuseppe',
    'cognome': 'Gialli',
    'telefono': '3330987654'
})

nome = input('Inserisci il nome del contatto da cercare: ')
cognome = input('Inserisci il cognome del contatto da cercare: ')
for contatto in rubrica:
    if contatto['nome'] == nome and contatto['cognome'] == cognome:
        numero = input('Inserisci il nuovo numero di telefono: ')
        contatto['telefono'] = numero
        break
else:
    print('Contatto non trovato')

for contatto in rubrica:
    print(contatto['nome'], contatto['cognome'], contatto['telefono'])    

