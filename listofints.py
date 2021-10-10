"""
https://www.reddit.com/r/learnpython/comments/q51ztn/sorting_without_using_inbuilt_commands/
"""

class ListOfInts:
    def __init__(self) -> None:
        self.items = []

    def add(self, item) -> None:
        """Add an item into the list keeping it sorted."""
        if len(self.items) == 0:
            self.items.append(item)
        else:
            # Find index where item should be inserted
            idx = 0
            while idx < len(self.items) and self.items[idx] < item:
                idx += 1

            # Build new list            
            self.items = self.items[:idx] + [item] + self.items[idx:]
    
obj = ListOfInts()
data = [45, 2, 8, 23, 89, 23, 7]
for each in data:
    obj.add(each)
print(obj.items)
