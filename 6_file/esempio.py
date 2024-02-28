# importare il modulo json
import json


# lettura da file JSON
with open(file="esempio.json", mode="r") as file_json:
    # usando un try-except riusciamo a gestire il caso in cui il file sia
    # inizialmente vuoto
    # mylist = json.load(file_json)
    try:
        mylist = json.load(file_json)
    except:
        mylist = []

# Stampa contenuto file JSON
print(type(mylist))
print(mylist)

mylist.append({"name": "Loredana", "surname": "Borselli", "age": 45, "hobbies": ["cars", "music", "computers"]})

# Scrittura sul file del contenuto aggiornato
with open("file_json.json", "w") as file_json:
    json.dump(obj=mylist, fp=file_json, indent=4)
