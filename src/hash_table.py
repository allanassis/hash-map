"""Basic of hash table only accepts integer as key"""

class HashTable():
    def __init__(self):
        self.tam = 10
        self._list = [None]*self.tam

    def insert(self, key, value):
        index = self._hash(key)
        self._list[index] = value
    
    def get(self, key):
        index = self._hash(key)
        return self._list[index]
    
    def delete(self, key):
        index = self._hash(key)
        self._list[index] = None

    def _hash(self, key):
        return int(key) % self.tam
