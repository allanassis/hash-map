# make hash table dynamic

class HashTable():
    def __init__(self):
        self.tam = 5
        self.used_slots = 0
        self._list = [None]*self.tam
    
    def insert(self, key, value):
        if self.used_slots == self.tam:
            self.__extend_map()
        index = self._hash(key)
        self._list[index] = (key, value)
        self.used_slots = self.used_slots + 1
    
    def __extend_map(self):
        self.tam = self.tam*2
        _new_list = [None]*self.tam
        for key, value in self._list:
            index = self._hash(key)
            _new_list[index] = (key, value)
        self._list = _new_list

    def get(self, key):
        index = self._hash(key)
        if self._list[index] is not None:
            return self._list[index][1]
        return None
    
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

