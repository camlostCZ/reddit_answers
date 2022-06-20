"""
https://www.reddit.com/r/pythonhelp/comments/vgr0wa/honestly_have_no_clue_whats_wrong_with_this/
"""

from locale import currency

CURRENCY_RATES = {
    "yen": 162.89,
    "yuan": 8.2199,
    "euro": 1.1657,
    "usd": 1.21
}


def conversion(amount: float, currency: str) -> float:
    cur_rate = CURRENCY_RATES[currency]
    result = cur_rate * amount
    return result


def main() -> None:
    money = int(input("How much money do you want to convert? (in pounds)\n"))
    currency = input("What currency do you want to convert too? (yuan,euro,usd or yen)\n")

    if currency in CURRENCY_RATES:
        amount = conversion(money, currency)
        print(f"You will get {amount} {currency}.")
    else:
        print("You inputted the currency incorrectly, please try again")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted by user.")
