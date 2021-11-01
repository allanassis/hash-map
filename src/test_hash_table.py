import unittest
from hash_table import HashTable


class TestHashTableV1(unittest.TestCase):
    def setUp(self):
        self.key = 123
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
        self.assertIn(self.value, h._list)

    def test_get(self):
        # arrange
        h = HashTable()
        h.insert(self.key, self.value)
        # act
        value = h.get(self.key)
        # assert
        self.assertEqual(value, self.value)
    
    def test_delete(self):
        # arrange
        h = HashTable()
        h.insert(self.key, self.value)
        # act
        h.delete(self.key)
        # assert
        self.assertIsNone(h.get(self.key))

if __name__ == '__main__':
    unittest.main()