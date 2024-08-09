import random

class RandomizedSet:

    def __init__(self):
        self.bag = set()

    def insert(self, val: int) -> bool:
        if val in self.bag:
            return False
        else:
            self.bag.add(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.bag:
            self.bag.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.sample(sorted(self.bag), 1)[0]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()