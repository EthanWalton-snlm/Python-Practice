# Task 1


def greet(name):
    return f"Hi {name}! 👋"


print(greet("Ethan"))


# Task 2


def driving_test(name, age):
    return (
        f"{name} is eligible for driving."
        if age >= 18
        else "Try again after few years 👶🍼"
    )


print(driving_test("Ethan", 21))

# Task 3


def pattern2(symbol, rows):
    return "\n".join([(i * symbol) for i in range(1, rows + 1) if rows > 0])


def pattern(symbol, rows):
    if rows <= 0:
        return ""

    res = symbol
    for i in range(2, rows + 1):
        res += "\n" + (symbol * i)

    return res


print(pattern("🥔", 3))
print(pattern2("🥔", 3))

# Task 4


def greet2(names):
    return "\n".join([f"Hi {name}! 👋" for name in names])


names = ["Anita", "Jamie", "Divyali", "Siyanda"]

print(greet2(names))

# Task 5

library_list = [
    {
        "title": "Python Programming",
        "author": "Eric Matthes",
        "year": 2019,
        "available": True,
    },
    {
        "title": "Automate the Boring Stuff with Python",
        "author": "Al Sweigart",
        "year": 2020,
        "available": True,
    },
    {
        "title": "Learning Python I",
        "author": "Mark Lutz",
        "year": 2013,
        "available": False,
    },
    {
        "title": "Fluent Python",
        "author": "Luciano Ramalho",
        "year": 2015,
        "available": True,
    },
    {
        "title": "Adavance Python",
        "author": "Mark Lutz",
        "year": 2015,
        "available": False,
    },
]

# Welcome to our Library app
# Main menu:

# 1. Add book to the library
# 2. Print all the books
# 3. Exit

# Please choose an option:

# if 1:
# Please tell me the title
# Please tell me the author
# Please tell me the year
# Please tell me if it is available? (True/False)

# Successfully added😄✅
# go back to main menu and repeat

# if 2:
# print and repeat

# if 3:
# Bye(emojis) then exit


def show_menu():
    print("Main menu:\n1. Add book to the library\n2. Print all the books\n3. Exit\n")
    return int(input("Please choose an option: "))


def add_book():
    title = input("Please tell me the title: ")
    author = input("Please tell me the author: ")
    year = int(input("Please tell me the year: "))
    available = bool(input("Please tell me if it is available? (True/False): "))

    library_list.append(
        {
            "title": title,
            "author": author,
            "year": year,
            "available": available,
        }
    )


def print_books():
    for book in library_list:
        print(
            f"{book['title']} by {book['author']} ({book['year']}) [Available: {book['available']}]"
        )


print("Welcome to our Library app\n")

while True:
    option = show_menu()
    print("\n")

    if option == 1:
        add_book()
        print("Successfully added😄✅\n")
    elif option == 2:
        print_books()
        print("\n")
    elif option == 3:
        print("Bye 😄👋")
        break
