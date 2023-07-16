"""
A cat walking in a maze
https://www.reddit.com/r/pythonhelp/comments/14zueyy/code_exceeding_maximum_processing_time/
"""

from os import system, name
from time import sleep
from typing import Callable, Optional

# I'm lazy to input the very same strings each time I need
# to debug my code so I stored them in these files.
LIST_SCENARIOS = [
    ("resources/walking_cat_map01.txt", 3),
    ("resources/walking_cat_map02.txt", 4),
    ("resources/walking_cat_map03.txt", 0),
    ("resources/walking_cat_map04.txt", 2),
    ("resources/walking_cat_map05.txt", 4),
    ("resources/walking_cat_map06.txt", 4),
    ("resources/walking_cat_map07.txt", 5),
    ("resources/walking_cat_map08.txt", 35),
    ("resources/walking_cat_map09.txt", 16),
    ("resources/walking_cat_map10.txt", 59)
]

SYMBOL_CAT = 'G'
SYMBOL_SNACK = '*'
SYMBOL_FLOOR = '_'
SYMBOL_HOLE = '.'


def clear_screen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def display_map(map: list[str], position: int, floor: int) -> None:
    clear_screen()
    for idx, row in enumerate(map):
        level = row
        if idx == floor:    # Replace current position with cat
            level = row[:position] + SYMBOL_CAT + row[position + 1:]
        print(level.strip())
    # Wait a moment
    sleep(1)


def verify_map_level(level: str) -> bool:
    without_floor = level.replace(SYMBOL_FLOOR, '')
    return len(without_floor) == 0


def walk_through_map(map: list[str], display_fn: Optional[Callable] = None,
        position: int = 0, direction: int = 1) -> int:
    result = 0
    if len(map) > 0:    # If map has some floors
        level_idx = 0
        level = map[level_idx].strip()  # Remove CRLF at the end of the string

        while True:
            if verify_map_level(level):
                # Not in the assignment but we can have some fun, can't we?
                print(f"The cat died from starvation. He cannot escape floor #{level_idx}.")
                break

            if display_fn:  # Display current state 
                display_fn(map, position, level_idx)

            current_symbol = level[position]
            if current_symbol == SYMBOL_HOLE:
                level_idx += 1
                if level_idx == len(map):   # End of map reached
                    break
                level = map[level_idx].strip()
            elif current_symbol == SYMBOL_SNACK:
                    result += 1
                    # Replace food symbol with floor symbol
                    level = level[:position] + SYMBOL_FLOOR + level[position + 1:]
                    # Update map so that the updated floor can be displayed
                    map[level_idx] = level
            elif current_symbol == SYMBOL_FLOOR:
                if direction == 1 and position + 1 == len(level):   # At the right end
                    direction = -1
                if direction == -1 and position == 0:   # At the left end
                    direction = 1
                position += direction
            else:   # Unknown symbol
                raise ValueError(f"Invalid map symbol {current_symbol} encountered.")

    return result


def main() -> None:
    map_id = 9
    # If all the maps should be run, remove the slice at the end of this line:
    for (map_path, expected) in LIST_SCENARIOS[map_id - 1:map_id]:
        print(f"\nMap: {map_path}")
        with open(map_path) as map_file:
            result = walk_through_map(map_file.readlines(), display_fn=display_map)
            print(f"Result / Expected:  {result} / {expected} ")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted by user.")