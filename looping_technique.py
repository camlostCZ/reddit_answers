"""
Looping Technique
https://www.reddit.com/r/learnpython/comments/wwghgt/looping_technique/
"""

DATA_SAMPLE = [
    "item_1", 350, "item_3", 
    47784, "item_5", 'item_6', 
    480, "item_8", 983843, "item_10"]


def filter_list(l):
    result = []
    for idx in range(0, len(l), 5):
        slice = l[idx:idx + 3]
        result += slice
    return result
        

def main() -> None:
    filtered = filter_list(DATA_SAMPLE)
    print(filtered)


if __name__ == "__main__":
    main()
