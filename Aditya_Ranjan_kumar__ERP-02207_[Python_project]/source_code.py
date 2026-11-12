rates_to_inr = {
    "INR":  1.0,
    "USD": 83.0,
    "EUR": 90.0,
    "GBP": 105.0
}


def convert_to_inr(amount, from_currency):
    return amount * rates_to_inr[from_currency]


def convert_currency(amount, from_currency, to_currency):
    amount_in_inr = convert_to_inr(amount, from_currency)
    convert_amount = amount_in_inr / rates_to_inr[to_currency]
    return round(convert_amount, 2)

def validate_currency(code):
    if code not in rates_to_inr:
        available = ", ".jion(rates_to_inr)
        print(f"Unsupported currency '{code}'. Available:{available}")
        return False
    return True

def format_amount(val):
    if val == int(val):
        return str(int(val))
    return str(val)


def main():
    amount_input = input("Amount: ").strip()
    try:
        amount = float(amount_input)
    except ValueError:
        print("Invalid amount. Enter a number.")
        return
    if amount < 0:
        print("Amount cannot be negative.")
        return

    from_currency = input("From: ").strip().upper()
    if not validate_currency(from_currency):
        return

    to_currency = input("To: ").strip().upper()
    if not validate_currency(to_currency):
        return

    result = convert_currency(amount, from_currency, to_currency)
    display_amount = format_amount(amount)
    print(f"{display_amount} {from_currency} = {result:.2f} {to_currency}")

if __name__ == "__main__":
    main()