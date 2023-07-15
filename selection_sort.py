"""
Selection Sort
"""

import random


def selection_sort(data: list[int]) -> list[int]:
    if len(data) > 1:
        for x in range(len(data) - 1):
            min_idx = x
            for idx in range(x + 1, len(data)):
                if data[idx] < data[min_idx]:
                    min_idx = idx
            data[x], data[min_idx] = data[min_idx], data[x]     # Swap values
    return data


data = random.choices(range(100), k=50000)
#print(f"Data sample:\n{data}")

sorted_data = selection_sort(data)
print(f"Sorted:\n{sorted_data}")
