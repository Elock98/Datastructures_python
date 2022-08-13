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
        pass

#-------------------------------------------------------------------#

    def test__hash(self):
        pass

#-------------------------------------------------------------------#

    def test_get(self):
        pass

#-------------------------------------------------------------------#

    def test_remove(self):
        pass

#-------------------------------------------------------------------#


if __name__ == "__main__":
    unittest.main()