"""Basic of hash table only accepts string as key with validation"""

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
        self._validate_key(key)
        ascii_key = sum([ord(c) for c in key])
        return ascii_key % self.tam
    
    def _validate_key(self, key):
        key_type = type(key)
        if key_type is not str:
            raise Exception(f"Type of key is {key_type}. Key must be a string!")

