"""
Given the following daily costs for a beach service:
- Umbrella: 12 euros
- Sunbed: 5 euros
- Deck chair: 6.50 euros

The task is to ask the user for the number of days and the services they want to book,
and then calculate and display the total cost.
"""

days = int(input("Enter number of vacation days: "))
umbrellas = int(input("How many umbrellas? "))
sunbeds = int(input("How many sunbeds? "))
deck_chairs = int(input("How many deck chairs? "))

umbrella_price = 12
sunbed_price = 5
deck_chair_price = 6.50

total_cost = days * ((umbrellas * umbrella_price) + (sunbeds * sunbed_price) + (deck_chairs * deck_chair_price))
print(total_cost)
