# handling collision

class HashTable():
    def __init__(self):
        self.tam = 5
        self.used_slots = 0
        self._list = [None]*self.tam
    
    def insert(self, key, value):
        if self.used_slots == self.tam:
            self.__extend_map()
        index = self._hash(key)

        if self._has_collision(index):
            index = self._resolve_collision(index)

        self._list[index] = (key, value)
        self.used_slots = self.used_slots + 1
    
    def __extend_map(self):
        self.tam = self.tam*2
        _new_list = [None]*self.tam
        for key, value in self._list:
            index = self._hash(key)
            _new_list[index] = (key, value)
        self._list = _new_list

    def _has_collision(self, index):
        if self._list[index] is not None:
            return True
        return False

    def _resolve_collision(self, collision_index):
        for i in range(collision_index, self.tam - 1):
            if self._list[i] is None:
                return i
        self.__extend_map()

        return self.tam/2

    def get(self, key):
        index = self._hash(key)
        item = self._list[index]
        if item is not None and item[0] == key:
            return item[1]
        for item in self._list:
            if item is not None and item[0] == key:
                return item[1]
        raise KeyError(f"Key not found {key}!")
    
    def delete(self, key):
        index = self._hash(key)
        k,v = self._list[index]
        if key == k:
            self._list[index] = None
            return
        for item in self._list:
            if item is not None and item[0] == key:
                self._list[index] = None

    def _hash(self, key):
        self._validate_key(key)
        ascii_key = sum([ord(c) for c in key])
        return ascii_key % self.tam
    
    def _validate_key(self, key):
        key_type = type(key)
        if key_type is not str:
            raise KeyError(f"Type of key is {key_type}. Key must be a string!")
