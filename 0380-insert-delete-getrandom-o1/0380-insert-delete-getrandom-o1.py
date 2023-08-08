import random
class RandomizedSet:
    def __init__(self):
        self.dct = {}

    def insert(self, val: int) -> bool:
        if val in self.dct:
            return False
        self.dct[val] = 0
        return True
        
    def remove(self, val: int) -> bool:
        if val in self.dct:
            self.dct.pop(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(list(self.dct.keys()))
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()