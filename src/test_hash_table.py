import unittest
from hash_table import HashTable


class TestHashTable(unittest.TestCase):
    def setUp(self):
        self.invalid_key = 123
        self.key = "Rei dos piratas"
        self.value = "Monkey D. Luffy"

    def test_instance(self):
        # arrange / act
        h = HashTable()
        # assert
        self.assertIsInstance(h, HashTable)

    def test_insert(self):
        # arrange
        h = HashTable()
        # act
        h.insert(self.key, self.value)
        # assert
        self.assertIn((self.key, self.value), h._list)

    def test_insert_many(self):
        # arrange
        h = HashTable()
        # act
        for i in range(0, 22, 2): # generate more than ten items in hash map with no collision
            h.insert(str(i),i)
        # assert
        for i in range(0, 22, 2):
            self.assertEqual(i, h.get(str(i)))

    def test_insert_with_invalid_key(self):
        # arrange
        h = HashTable()
        # assert
        with self.assertRaises(Exception):
            # act
            h.insert(self.invalid_key, self.value)

    def test_get(self):
        # arrange
        h = HashTable()
        h.insert(self.key, self.value)
        # act
        value = h.get(self.key)
        # assert
        self.assertEqual(value, self.value)
    
    def test_get_with_invalid_key(self):
        # arrange
        h = HashTable()
        h.insert(self.key, self.value)
        # assert
        with self.assertRaises(Exception):
            # act
            h.get(self.invalid_key)

    def test_delete(self):
        # arrange
        h = HashTable()
        h.insert(self.key, self.value)
        # act
        h.delete(self.key)
        # assert
        self.assertIsNone(h.get(self.key))

    def test_delete_with_invalid_key(self):
        # arrange
        h = HashTable()
        h.insert(self.key, self.value)
        # assert
        with self.assertRaises(Exception):
            # act
            h.delete(self.invalid_key)

if __name__ == '__main__':
    unittest.main()