# https://leetcode.com/problems/design-hash-map/description/

class MyHashMap:
    def __init__(self):
        self.hashmap = [-1] * 1000001 # Since keys are constrained to the range [0, 1000000]

    def put(self, key: int, value: int) -> None:
        self.hashmap[key] = value

    def get(self, key: int) -> int:
        return self.hashmap[key]

    def remove(self, key: int) -> None:
        self.hashmap[key] = -1