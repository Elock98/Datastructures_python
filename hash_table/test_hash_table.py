import unittest

from hash_table import HashTable
from unittest.mock import patch


class TestHashTable(unittest.TestCase):

#-------------------------------------------------------------------#

    def test_creation_bad_function(self):
        # Given / When
        with self.assertRaises(Exception) as ex:
            table = HashTable("foo", 5)

        # Then
        self.assertEqual(str(ex.exception),
                        "Hash function needs to be callable!")

    def test_creation_bad_table_lenght_type(self):
        # Given / When
        with self.assertRaises(Exception) as ex:
            table = HashTable(lambda:5, "foo")

        # Then
        self.assertEqual(str(ex.exception),
                        "Table length needs to be of type int!")

    def test_creation_bad_table_lenght(self):
        # Given / When
        with self.assertRaises(Exception) as ex:
            table = HashTable(lambda:5, -123)

        # Then
        self.assertEqual(str(ex.exception),
                        "Table length needs to be larger than 0!")

    def test_creation_bad_chaining(self):
        # Given / When
        with self.assertRaises(Exception) as ex:
            table = HashTable(lambda:5, 5, "foo")

        # Then
        self.assertEqual(str(ex.exception),
                        "Chaning needs to be of type bool!")

    def test_creation(self):
        # Given
        fun = lambda:5

        # When
        table = HashTable(fun, 5, True)

        # Then
        self.assertTrue(callable(table._hash_function))
        self.assertEqual(table._hash_function, fun)
        self.assertEqual(table._table_langth, 5)
        self.assertEqual(table._chaining, True)
        self.assertEqual(table._hash_table, [[]] * 5)

#-------------------------------------------------------------------#

    def test_insert(self):
        # Given
        table = HashTable(lambda key: len(key), 10)

        # When
        table.insert("foo", 100)

        # Then
        self.assertEqual(table._hash_table, [None,
                                             None,
                                             None,
                                             ("foo", 100),
                                             None,
                                             None,
                                             None,
                                             None,
                                             None,
                                             None])

    def test_insert_chaining(self):
        # Given
        table = HashTable(lambda key: len(key), 10, True)

        # When
        table._insert_chaining("foo", 100)

        # Then
        self.assertEqual(table._hash_table, [[],
                                             [],
                                             [],
                                             [("foo", 100)],
                                             [],
                                             [],
                                             [],
                                             [],
                                             [],
                                             []])

    def test_insert_chaining_collision(self):
        # Given
        table = HashTable(lambda key: len(key), 10, True)
        table._hash_table = [[],
                             [],
                             [],
                             [("foo", 100)],
                             [],
                             [],
                             [],
                             [],
                             [],
                             []]
        # When
        table._insert_chaining("bar", 200)

        # Then
        self.assertEqual(table._hash_table, [[],
                                             [],
                                             [],
                                             [("foo", 100), ("bar", 200)],
                                             [],
                                             [],
                                             [],
                                             [],
                                             [],
                                             []])

    def test_insert_linear_probing(self):
        # Given
        table = HashTable(lambda key: len(key), 10)

        # When
        table._insert_linear_probing("foo", 100)

        # Then
        self.assertEqual(table._hash_table, [None,
                                             None,
                                             None,
                                             ("foo", 100),
                                             None,
                                             None,
                                             None,
                                             None,
                                             None,
                                             None])

    def test_insert_linear_probing_collision(self):
        # Given
        table = HashTable(lambda key: len(key), 10)

        # When
        table._insert_linear_probing("foo", 100)
        table._insert_linear_probing("bar", 200)

        # Then
        self.assertEqual(table._hash_table, [None,
                                             None,
                                             None,
                                             ("foo", 100),
                                             ("bar", 200),
                                             None,
                                             None,
                                             None,
                                             None,
                                             None])

    def test_insert_linear_probing_full(self):
        # Given
        table = HashTable(lambda key: len(key), 3)

        # When
        table._insert_linear_probing("foo", 100)
        table._insert_linear_probing("bar", 200)
        table._insert_linear_probing("baz", 300)
        with self.assertRaises(Exception) as ex:
            table._insert_linear_probing("faz", 400)

        # Then
        self.assertEqual(table._hash_table, [("foo", 100),
                                             ("bar", 200),
                                             ("baz", 300)])
        self.assertEqual(str(ex.exception), "Hash table is full!")

#-------------------------------------------------------------------#

    def test__hash(self):
        # Given
        table = HashTable(lambda x: sum([ord(i)%5 for i in x]), 5)

        # When
        index = table._hash("foo")

        # Then
        self.assertEqual(index, 4)

#-------------------------------------------------------------------#

    def test_get_chaining(self):
        # Given
        table = HashTable(lambda x: 3, 5, True)
        table._hash_table = [[],
                             [],
                             [],
                             [("foo", 100), ("bar", 200)],
                             [],
                             [],
                             [],
                             [],
                             [],
                             []]

        # When
        value = table._get_chaining("bar")

        # Then
        self.assertEqual(value, 200)

    def test_get_chaining_not_in_table(self):
        # Given
        table = HashTable(lambda x: 3, 5, True)
        table._hash_table = [[],
                             [],
                             [],
                             [("foo", 100)],
                             [],
                             []]

        # When
        with self.assertRaises(Exception) as ex:
            value = table._get_chaining("bar")

        # Then
        self.assertEqual(str(ex.exception), "Key not in hash table!")

    def test_get_linear(self):
        # Given
        table = HashTable(lambda x: 3, 5, False)
        table._hash_table = [None,
                             None,
                             None,
                             ("foo", 100),
                             None]

        # When
        value = table._get_linear_probing("foo")

        # Then
        self.assertEqual(value, 100)

    def test_get_linear_collision(self):
        # Given
        table = HashTable(lambda x: 3, 5, False)
        table._hash_table = [("baz", 300),
                             None,
                             None,
                             ("foo", 100),
                             ("bar", 200)]

        # When
        value = table._get_linear_probing("baz")

        # Then
        self.assertEqual(value, 300)

    def test_get_linear_not_in_table(self):
        # Given
        table = HashTable(lambda x: 3, 5, False)
        table._hash_table = [None,
                             None,
                             None,
                             ("foo", 100),
                             None]

        # When
        with self.assertRaises(Exception) as ex:
            value = table._get_linear_probing("bar")

        # Then
        self.assertEqual(str(ex.exception), "Key not in hash table!")

#-------------------------------------------------------------------#

    def test_remove_chaining(self):
        # Given
        table = HashTable(lambda x: 3, 5, True)
        table._hash_table = [[],
                             [],
                             [],
                             [("foo", 100), ("bar", 200)],
                             [],
                             [],
                             [],
                             [],
                             [],
                             []]

        # When
        table._remove_chaining("foo")

        # Then
        self.assertEqual(table._hash_table, [[],
                                             [],
                                             [],
                                             [("bar", 200)],
                                             [],
                                             [],
                                             [],
                                             [],
                                             [],
                                             []])

    def test_remove_chaining_not_in_table(self):
        # Given
        table = HashTable(lambda x: 3, 5, True)
        table._hash_table = [[],
                             [],
                             [],
                             [("foo", 100), ("bar", 200)],
                             [],
                             [],
                             [],
                             [],
                             [],
                             []]

        # When
        with self.assertRaises(Exception) as ex:
            table._remove_chaining("baz")

        # Then
        self.assertEqual(str(ex.exception), "Key not in hash table!")
        self.assertEqual(table._hash_table, [[],
                                             [],
                                             [],
                                             [("foo", 100), ("bar", 200)],
                                             [],
                                             [],
                                             [],
                                             [],
                                             [],
                                             []])

    def test_remove_linear(self):
         # Given
        table = HashTable(lambda x: 3, 5, False)
        table._hash_table = [None,
                             None,
                             None,
                             ("foo", 100),
                             None]

        # When
        table._remove_linear("foo")

        # Then
        self.assertEqual(table._hash_table, [None,
                                             None,
                                             None,
                                             None,
                                             None])

    def test_remove_linear_not_in_table(self):
        # Given
        table = HashTable(lambda x: 3, 5, False)
        table._hash_table = [None,
                             None,
                             None,
                             ("foo", 100),
                             None]

        # When
        with self.assertRaises(Exception) as ex:
            table._remove_linear("bar")

        # Then
        self.assertEqual(str(ex.exception), "Key not in hash table!")
        self.assertEqual(table._hash_table, [None,
                                             None,
                                             None,
                                            ("foo", 100),
                                             None])

#-------------------------------------------------------------------#


if __name__ == "__main__":
    unittest.main()