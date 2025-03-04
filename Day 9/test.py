books = [
    {"title": "1984", "author": "George Orwell", "year": 1949},
    {"author": "J.K. Rowling"},  # Missing title and year
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
    {"title": "To Kill a Mockingbird", "year": 1960},  # Missing author
    {"author": "Ernest Hemingway", "year": 1952},  # Missing title
]

# Task 1.2 - Method 1


def format_books(books):
    result = ""
    for book in books:
        result += f"'{book.get('title', 'Untitled')}' by {book.get('author', 'Unknown')} ({book.get('year', 'N/A')})\n"

    return result


print(format_books(books))

# Task 1.2 - Method 2


def format_books2_helper(title="Untitled", author="Unknown", year="N/A"):
    return f"'{title}' by {author} ({year})\n"


def format_books2(bks):
    res = ""
    for book in bks:
        res += format_books2_helper(**book)

    return res


print("\n---\nMethod 2:\n---\n" + format_books2(books))

# Task 1.2 - Method 3


def format_books3(books):
    result = ""
    for book in books:
        result += format_books2_helper(book.items())

    return result


def format_books3_helper(*vals):
    title = vals[0] if len(vals) >= 0 else "Untitled"
    author = vals[1] if len(vals) >= 1 else "Unknown"
    year = vals[2] if len(vals) >= 2 else "N/A"

    return f"'{title}' by {author} ({year})\n"


print(format_books3(books))
