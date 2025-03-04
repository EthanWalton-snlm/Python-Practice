from datetime import datetime

items = [
    {"name": "Widget A", "quantity": 10, "price": 2.5},
    {"name": "Widget B", "quantity": 5, "price": 15.75},
    {"name": "Gadget", "quantity": 2, "price": 99.99},
]


def print_invoice(invoice_date, items):
    result = f"Invoice Date: {invoice_date:%d %B %Y}\n"
    result += f"{'Product':<25}{'Qty':<5}{'Unit Price':>15}{'Total':>15}\n"

    result += "-" * 60 + "\n"
    total = 0

    for item in items:
        result += f"{item['name']:<25}{item['quantity']:<5}{item['price']:>15}{item['quantity'] * item['price']:>15}\n"
        total += item["quantity"] * item["price"]
        # result += f"{item['name']}\t{item['quantity']:>}\t{item['price']}\t{item['quantity'] * item['price']:>7}\n"

    result += "-" * 60 + "\n"

    result += f"{'Grand Total':<30}{total:>30}"
    return result


print(print_invoice(datetime.now(), items))
