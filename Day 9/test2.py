recipe = {
    "name": "Spaghetti Carbonara",
    "servings": 4,
    "ingredients": [
        "200g spaghetti",
        "100g pancetta",
        "2 eggs",
        "1/2 cup grated Parmesan",
        "1 clove garlic",
    ],
}


def format_recipe():
    name = f" {recipe['name']} "
    print(f"{name:=^34}")
    for ingredient in recipe["ingredients"]:
        print(f"- {ingredient}")

    print(f"Serves: {recipe['servings']} people")


format_recipe()

# Task 1
# ======= Spaghetti Carbonara =======
# - 200g spaghetti
# - 100g pancetta
# - 2 eggs
# - 1/2 cup grated Parmesan
# - 1 clove garlic
# Serves: 4 people
