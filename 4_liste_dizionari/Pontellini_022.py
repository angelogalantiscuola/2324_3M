#Esercizio: 
#Attività 1: Creare un dizionario.
#Inizia creando un dizionario. Questo dizionario dovrebbe rappresentare un libro. Utilizzare tasti come title, author, e year published e assegnare loro i valori appropriati.

#Attività 2: Aggiungere un elemento.
#Aggiungere una nuova coppia chiave-valore al dizionario. La chiave dovrebbe essere gender e il valore dovrebbe essere qualsiasi genere a tua scelta.

#Attività 3: Modificare un elemento
#Modificare il valore di una delle chiavi esistenti nel dizionario. Ad esempio, è possibile modificare il valore della chiave year_published in un anno diverso.

#Attività 4: Eliminare un elemento.
#Rimuovere una coppia chiave-valore dal dizionario. Ad esempio, è possibile rimuovere la chiave author.

#Attività 5: Scorrere il dizionario.
#Scrivi tre cicli separati:
#Uno per stampare tutte le chiavi keys()
#Uno per stampare tutti i valori values()
#Uno per stampare tutte le coppie chiave-valore (elementi) nel dizionario items()
#Ricorda, i metodi del dizionario di Python title, author, e year_published saranno utili in questo compito. 

import os

book = {

}

while True:

    os.system ('cls'if os.name == 'nt' else 'clear')
    
    print ("""
    1) Create a dictionary
    2) Add an item
    3) Edit an item
    4) Delete an item
    5) Scroll through the dictionary""")

    choise = input ("Choose the option you want: '")

    match choise:

        case '1':

            print ("Create a dictionary")

            answer_1 = str (input ("Do you want to create a new dictionary? '"))

            if answer_1 == "Yes":

                book = dict (title = "There is no title of the book" , author = "The author's name is not present" , year_published = "The year of publication of the book is not present")

                book.update (book)

                print (f"{book}")

            elif answer_1 == "No":

                print ("The book was not created")

                print (f"{book}")
        
            else: print ("Error")
        
        case '2':

            print ("Add an item")

            answer_2 = str (input ("Do you want to add an item? '"))

            if answer_2 == "Yes":

                genders = str (input ("Enter the genre of the book: '")) 
                
                book ["gender"] = genders 

                print (f"{book}")

            elif answer_2 == "No":

                print ("No genre has been added to the book")

                print (f"{book}")
            
            else: print ("Error")
        
        case '3':

            print ("Edit an item")

            answer_3 = str (input ("Do you want to edit the item? '"))

            if answer_3 == "Yes":

                answer_4 = str (input ("Do you want to add a title, an author and a year of publication to the book? '"))

                if answer_4 == "Yes":

                    title = str (input ("Enter the title of book: '"))
                    author = str (input ("Enter the author of the book: '"))
                    year_published = int (input ("Enter the year published of the book: '"))

                    book ["title"] = title
                    book ["author"] = author
                    book ["year_published"] = year_published

                    TITLE = title
                    AUTHOR = author
                    YEAR_PUBLISHED = year_published

                elif answer_4 == "No":

                    print ("No changes will be made")

                    print (f"{book}")

                else: print ("Error")

            elif answer_3 == "No":

                print ("No items have been edited")

                print (f"{book}")
            
            else: print ("Error")
        
        case '4':

            print ("Delete an item")

            answer_5 = str (input ("Do you want to delete an item? '")) 

            if answer_5 == "Yes":

                print (f"{book}")

                TITLE = title
                AUTHOR = author
                YEAR_PUBLISHED = year_published

                book ["title"] = title
                book ["author"] = author
                book ["year_published"] = year_published

                items = book.items ()

                answer_6 = str (input ("What do you want to delete from the dictionary?\n The title?\n The author?\n The year published or the genre? '")) 

                if answer_6 == "Title":

                    book.pop ("title", None)

                    print ("The title has been removed.")

                    print (f"{book}")
                
                elif answer_6 == "Author":

                    book.pop ("author", None)

                    print ("The author has been removed.")

                    print (f"{book}")
                
                elif answer_6 == "Year published":

                    book.pop ("year_published", None)

                    print ("The year published has been removed.")

                    print (f"{book}")
                
                elif answer_6 == "Genre":

                    book.pop ("genre", None)

                    print ("The genre has been removed.")

                    print (f"{book}")
                
                else: print ("Error")
            
            elif answer_5 == "No":

                print ("No items have been deleted")

                print (f"{book}")
            
            else: print ("Error")
        
        case '5':

            print ("Scroll through the dictionary")

            answer_7 = str (input ("Do you want to scroll through the dictionary? '")) 

            while answer_7 == "Yes":

                if answer_7 == "Yes":

                    print ("What do you want to see of the book?\n All the keys?\n All values?\n Or all key-value pairs (items) in the dictionary?")

                    answer_8 = str (input ("Enter 'keys' if you want to see the keys:\n Enter 'values' if you want to see the values:\n Enter 'items' if you want to see the items:"))

                    if answer_8 == "keys":

                        keys = book.keys ()

                        for keys in keys:

                            print (f"{keys}") 

                        answer_9 = str (input ("Do you want to see something else? '"))

                        if answer_9 != "Yes" or answer_9 != "No": 
                            answer_7 == False

                            if answer_9 == "Yes":
                                answer_7 == True

                            elif answer_9 == "No":
                                answer_7 == False
                                break
                        
                            else: print ("Error")
                
                    elif answer_8 == "values":

                        values = book.values()

                        for values in (values):

                            print (f"{values}")
                        
                        answer_10 = str (input ("Do you want to see something else? '"))

                        if answer_10 != "Yes" or answer_10 != "No": 
                            answer_7 == False

                            if answer_10 == "Yes":
                                answer_7 == True

                            elif answer_10 == "No":
                                answer_7 == False
                                break
                        
                        else: print ("Error")
                
                    elif answer_8 == "items":

                        items = book.items ()

                        for items in (items):

                            print (f"{items}")
                        
                        answer_11 = str (input ("Do you want to see something else? '"))

                        if answer_11 != "Yes" or answer_11 != "No": 
                            answer_7 == False

                            if answer_11 == "Yes":
                                answer_7 == True

                            elif answer_11 == "No":
                                answer_7 == False
                                break
                        
                        else: print ("Error")
                
                    else: print ("Error")
            
                elif answer_8 == "No":

                    print ("You won't be able to scroll through the dictionary")
                    break

                else:

                    answer_8 = str (input ("Are you sure you want to do it? '"))

                    if answer_8 == "Yes":

                        print ("You won't be able to scroll through the dictionary")
                        break

                    elif answer_8 == "No":

                        print ("You will return to step 5")
                    
                    else: print ("Error")

        case _: print("Invalid choice.")
    input("Press enter to continue...")