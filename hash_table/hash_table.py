from typing import Callable

class HashTable:

    def __init__(self, hash_function:Callable[[], int],
                    table_length:int, chaining:bool=False) -> None:
        # Argument validation
        assert callable(hash_function), "Hash function needs to be callable!"
        assert isinstance(table_length, int), "Table length needs to be of type int!"
        assert table_length > 0, "Table length needs to be larger than 0!"
        assert isinstance(chaining, bool), "Chaning needs to be of type bool!"

        # Setting instance variables
        self._hash_function = hash_function
        self._table_langth = table_length
        self._chaining = chaining
        self._hash_table = []

    def insert(self, key, value) -> None:
        pass

    def _hash(self, key) -> int:
        pass

    def get(self, key):
        pass

    def remove(self, key):
        pass
    