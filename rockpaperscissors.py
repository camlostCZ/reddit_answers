import random

OPTIONS = ["rock", "paper", "scissors"]


def rock_paper_scissors(move_a: str, move_b: str, options: list[str]) -> int:
    result = 0  # A draw
    if (move_a != move_b):
        result = [-1, 1][move_b == options[(options.index(move_a) + 1) % len(options)]]
    return result


def main() -> None:
    m1, m2 = random.choice(OPTIONS), random.choice(OPTIONS)
    print(f"Move: {m1} vs. {m2}")
    print(f"Result: {rock_paper_scissors(m1, m2, OPTIONS)}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted by user.")
