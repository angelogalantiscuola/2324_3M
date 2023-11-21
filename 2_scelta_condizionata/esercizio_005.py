#ESERCIZIO 5
#Write a program that asks the user for their age and prints out whether they are a child (age 0-12), teenager (age 13-19), adult (age 20-64), or senior (age 65+)


age = input("insert age")

if age < 12:
    print ("child")
elif age < 19:
    print ("teenager")
elif age < 64:
    print ("adult")
else:
    print ("senior")
