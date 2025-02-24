# Task 1.3
stock1 = "vanilla"
stock2 = "chocolate"
stock3 = "tin roof"
stock4 = "cookie dough"

# Output
# Case 1
# Please enter your fav 🍧?: VAnilla
# Yes, we have vanilla in stock

# Case 2
# Please enter your fav 🍧?: salted Caramel
# Sorry, we ran out of Salted Caramel
# if in stock say yes, else say no we ran out

# Task 1.1

stock1 = "vanilla"
stock2 = "chocolate"
stock3 = "mint"
stock4 = "salted caramel"

flavour = input("Please enter your favourite 🍧?: ").strip().lower()
in_stock = False

if stock1 == flavour:
    in_stock = True
elif stock2 == flavour:
    in_stock = True
elif stock3 == flavour:
    in_stock = True
elif stock4 == flavour:
    in_stock = True

if in_stock:
    print(f"Yes, we have {flavour} in stock.")
else:
    print(f"Sorry, we ran out of {flavour}.")

# Task 1.2

stock1 = "vanilla"
stock2 = "chocolate"
stock3 = "mint"
stock4 = "salted caramel"

flavour = input("Please enter your favourite 🍧?: ").strip().lower()

if stock1 == flavour or stock2 == flavour or stock3 == flavour or stock4 == flavour:
    print(f"Yes, we have {flavour} in stock.")
else:
    print(f"Sorry, we ran out of {flavour}.")

# Task 1.3

stock1 = "vanilla"
stock2 = "chocolate"
stock3 = "mint"
stock4 = "salted caramel"

flavour = input("Please enter your favourite 🍧?: ").strip().lower()

if flavour in (stock1, stock2, stock3, stock4):
    print(f"Yes, we have {flavour} in stock.")
else:
    print(f"Sorry, we ran out of {flavour}.")

# Task 1.2

person_1 = input("What is the name of person 1? ")
person_1_height = float(input("What is the height of person 1? "))

person_2 = input("What is the name of person 2? ")
person_2_height = float(input("What is the height of person 2? "))

difference = abs(person_1_height - person_2_height)

if person_1_height > person_2_height:
    print(f"{person_1} is taller than {person_2} by {difference}cm")
elif person_1_height < person_2_height:
    print(f"{person_2} is taller than {person_1} by {difference}cm")
else:
    print(f"{person_1} and {person_2} are the same height.")


# Task 1.1

person_1 = input("What is the name of person 1? ")
person_1_height = float(input("What is the height of person 1? "))

person_2 = input("What is the name of person 2? ")
person_2_height = float(input("What is the height of person 2? "))

difference = abs(person_1_height - person_2_height)

if person_1_height > person_2_height:
    print(f"{person_1} is taller than {person_2} by {difference}cm")
else:
    print(f"{person_2} is taller than {person_1} by {difference}cm")
