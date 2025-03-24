# Task 4

progress = round(int(input("What is the progress out of 100? ")) / 10)

print("[" + ("=" * progress) + (" " * (10 - progress)) + "]")

# Task 1

fahrenheight = input("Please provide the temperature in Fahrenheit: ")

celsius = (float(fahrenheight) - 32) * 5 / 9

print(f"{fahrenheight}°F is {celsius}°C")

# Task 2

birth_year = input("Please enter your birth year: ")

age = 2025 - int(birth_year)

print(f"Your age is {age}")

# Task 3

PI = 3.14

radius = input("Provide the radius of the circle: ")

area = PI * (float(radius) ** 2)

print(f"The area of the circle is {area}")
