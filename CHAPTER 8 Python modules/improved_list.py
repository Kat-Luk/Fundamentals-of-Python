# Create a class called "ImprovedList" that contains the following member variables:
# - lst: list

# Besides the constructor, which must take a list as a parameter with a default value of an empty list, the class should also contain the following methods:
# shuffle(): Randomly shuffles the list in-place. Doesn't return anything.
# poprandom(): Pop a random value from the list. Returns the popped value.

import random
class ImprovedList:
    def __init__(self, lst = []):
        self.lst = lst
    def shuffle(self):
        random.shuffle(self.lst)
    def poprandom(self):
        index = random.randint(0,len(self.lst)-1)
        pop_el = self.lst[index]
        self.lst.pop(index)
        return pop_el