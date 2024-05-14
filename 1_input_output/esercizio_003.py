"""
The task is to ask the user for the radius of a circle,
and then calculate and display the circumference and the area of the circle.
"""

radius = float(input("Enter the radius: "))

circumference = 2 * 3.14 * radius
area = 3.14 * radius**2

print(f"Circumference: {circumference:.2f}")
print(f"Area: {area:.2f}")
