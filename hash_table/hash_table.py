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
        '''Inserts (key, value) into the hash table'''
        if self._chaining:
            self._insert_chaining(key, value)
        else:
            self._insert_linear_probing(key, value)

    def _insert_chaining(self, key, value) -> None:
        '''Insertion for chaining'''
        index = self._hash(key)

        self._hash_table[index].append((key, value))

    def _insert_linear_probing(self, key, value) -> None:
        '''Insertion for linear probing'''
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
        '''Runs the hashing function given at creation'''
        return self._hash_function(key)

    def get(self, key):
        '''Returns the value stored with key'''
        if self._chaining:
            return self._get_chaining(key)
        else:
            return self._get_linear_probing(key)

    def _get_chaining(self, key):
        '''Gets from chained hash table'''
        index = self._hash(key)

        for entry in self._hash_table[index]:
            if entry[0] == key:
                return entry[1]

        raise ValueError("Key not in hash table!")

    def _get_linear_probing(self, key):
        '''Gets from linear hash table'''
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
        '''Removes entry marked by key from the hash table'''
        if self._chaining:
            self._remove_chaining(key)
        else:
            self._remove_linear(key)

    def _remove_chaining(self, key):
        '''Removes from chained hash table'''
        index = self._hash(key)

        for pos, entry in enumerate(self._hash_table[index]):
            if entry[0] == key:
                del self._hash_table[index][pos]
                return

        raise ValueError("Key not in hash table!")

    def _remove_linear(self, key):
        '''Removes from linear hash table'''
        index = start_index = self._hash(key)

        while True:
            if index == len(self._hash_table):
                index = 0

            if self._hash_table[index] != None and\
                self._hash_table[index][0] == key:
                self._hash_table[index] = None
                return

            index += 1
            if index == start_index:
                raise ValueError("Key not in hash table!")

    def print_hash_table(self):
        '''Prints the hash table'''
        print(self._hash_table)