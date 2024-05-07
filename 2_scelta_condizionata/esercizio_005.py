"""
The task is to write a program that interacts with the user in the following way:

1. The program asks the user for their age.
2. Based on the input, the program categorizes the user into one of the following age groups and prints out the result:
    - Child (age 0-12)
    - Teenager (age 13-19)
    - Adult (age 20-64)
    - Senior (age 65+)
"""


def main():
    # Get the age from the user and convert it to an integer
    age = int(input("Insert your age: "))

    # Determine the age group and print it
    if age <= 12:
        print("Child")
    elif age <= 19:
        print("Teenager")
    elif age <= 64:
        print("Adult")
    else:
        print("Senior")


if __name__ == "__main__":
    main()
