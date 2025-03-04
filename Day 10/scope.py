# get_price
# First checks for `local` price variable
# Then checks outer scope (lexical scope)

# Closure = own scope + lexical scope

price = 100


def get_price():
    print("Price is ", price)


get_price()
