from datetime import datetime

items = [
    {"name": "Widget A", "quantity": 10, "price": 2.5},
    {"name": "Widget B", "quantity": 5, "price": 15.75},
    {"name": "Gadget", "quantity": 2, "price": 99.99},
]


def print_invoice(invoice_date=f"{datetime.now():%d %B %Y}", items=[{}]):
    result = f"\nInvoice Date: {invoice_date}\n{'Product':<25}{'Qty':<5}{'Unit Price':>15}{'Total':>15}\n{'-' * 60}\n"

    total = 0

    for item in items:
        result += f"{item['name']:<25}{item['quantity']:<5}{item['price']:>15}{item['quantity'] * item['price']:>15}\n"
        total += item["quantity"] * item["price"]

    result += f"{'-' * 60}\n{'Grand Total':<30}{total:>30}\n"
    return result


if __name__ == "__main__":
    print(print_invoice("3 March 2025", items))
