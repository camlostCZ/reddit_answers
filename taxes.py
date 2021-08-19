"""
https://www.reddit.com/r/learnpython/comments/p6bpbc/opinion_on_a_better_implementation_for_this/
"""

TAX_RATES = [
    {"limit": 0, "rate": 9},
    {"limit": 1000, "rate": 11},
    {"limit": 2000, "rate": 14}
]


def compute_tax(income: float, rates: list[dict[str, float]]) -> float:
    result = 0.0
    for item in reversed(rates):
        if income > item["limit"]:
            base = income - item["limit"]
            result += base * item["rate"] / 100.0
            income = income - base
    return result


def main():
    income = 2700.0
    tax = compute_tax(income, TAX_RATES)
    print(f"Income: {income}  ->  tax: {tax}")


if __name__ == "__main__":
    main()
