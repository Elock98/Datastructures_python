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

        if self._chaining:
            self._hash_table = [[] for _ in range(self._table_langth)]
        else:
            self._hash_table = [None] * self._table_langth

    def insert(self, key, value) -> None:
        if self._chaining:
            self._insert_chaining(key, value)
        else:
            self._insert_linear_probing(key, value)

    def _insert_chaining(self, key, value) -> None:
        index = self._hash(key)

        self._hash_table[index].append((key, value))

    def _insert_linear_probing(self, key, value) -> None:
        index = start_index = self._hash(key)

        while True:
            if index == len(self._hash_table):
                index = 0

            if self._hash_table[index] == None:
                self._hash_table[index] = (key, value)
                break

            index += 1
            if index == start_index:
                raise ValueError("Hash table is full!")

    def _hash(self, key) -> int:
        return self._hash_function(key)

    def get(self, key):
        if self._chaining:
            return self._get_chaining(key)
        else:
            return self._get_linear_probing(key)

    def _get_chaining(self, key):
        index = self._hash(key)

        for entry in self._hash_table[index]:
            if entry[0] == key:
                return entry[1]

        raise ValueError("Key not in hash table!")

    def _get_linear_probing(self, key):
        index = start_index = self._hash(key)

        while True:
            if index == len(self._hash_table):
                index = 0

            if self._hash_table[index] != None and\
                self._hash_table[index][0] == key:
                return self._hash_table[index][1]

            index += 1
            if index == start_index:
                raise ValueError("Key not in hash table!")

    def remove(self, key):
        pass
    