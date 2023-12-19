classe_3M_dict = [
  {
    "name": "Carol",
    "age": 28,
    "hobbies": ["painting", "yoga", "gardening", "reading"]
  },
  {
    "name": "Bob",
    "age": 32,
    "hobbies": ["soccer", "guitar", "cooking"]
  },
]

if False:
    # # stampa il nome del primo studente
    # print(classe_3M_dict[0]["name"]) # Carol

    # for i in range(len(classe_3M_dict)): # range(2) -> [0, 1]
    # print(f'studente numero {i+1}: {classe_3M_dict[i]["name"]}')

    for studente in classe_3M_dict:
        print(f'studente numero:{studente["numero"]} {studente["name"]}')

    for i, studente in zip(range(len(classe_3M_dict)), classe_3M_dict):
        print(f'studente numero:{i+1} {studente["name"]}')


# stampare gli hobby del secondo studente
print(classe_3M_dict[1]["hobbies"])
# stampare l'eta di tutti gli studenti
for studente in classe_3M_dict:
    print(studente["age"])
# stampare l'ultimo hobby del primo studente
print(classe_3M_dict[0]["hobbies"][2]) # type: ignore
print(classe_3M_dict[0]["hobbies"][-1]) # type: ignore

