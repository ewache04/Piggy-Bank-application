# utils.py
def validate_input(value):
    try:
        return float(value)
    except ValueError:
        return None


def calculate_gift_cards(total_amount, unit_price):
    return int(total_amount // unit_price)


def format_balance(balance):
    dollars = int(balance)
    cents = int((balance - dollars) * 100)
    return dollars, cents
