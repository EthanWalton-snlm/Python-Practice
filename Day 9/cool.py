def to_upper_case(text):
    """
    This is beautiful function that returns uppercase value with wave emoji
    """
    return text.upper() + " 👋"


#  Only when cool.py execute -> Jamie
# dunder variables


def main():
    # Specific cool.py code
    print(__name__)
    print(to_upper_case("Jamie"))


if __name__ == "__main__":
    main()

# Two values for __name__:
# Self execution    -  __name__ -> __main__
# From another file -  __name__ -> file name

# sum()
