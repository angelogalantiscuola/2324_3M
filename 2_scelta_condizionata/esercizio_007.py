def main():
     
    number_1 = int(input("inserire numero: "))
    number_2 = int(input("inserire numero: "))
    number_3 = int(input("inserire numero:"))

    if number_1>number_2 and number_1>number_3:
        print("il numero maggiore è", number_1)
    elif number_2>number_3 and number_2> number_1:
        print("il numero maggiore è", number_2)
    elif number_3>number_1 and number_3>number_2:
        print("il numero maggiore è", number_3)

if __name__ == "__main__":
        main()