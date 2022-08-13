# Homemade datastructures for python

__ __ _
>**This is a small project to practice
construction of, and to explore
usefull datastructures.**
>
__ __ _

Min heap
---------
__ __ _
The min heap is *created* by:

    from min_heap import MinHeap
    my_heap = MinHeap()

To *add* a value to the heap:

    my_heap.add(3)
    # The value 3 added to the heap

*Removing* from the heap can be done by
*value* or by *index*:

    my_heap.pop_index(0)
    # Root node removed

    my_heap.pop_value(3)
    # Removed node with value 3

The heap can be *displayed* as a list
by using:

    my_list.print_heap()
__ __ _


Hash table
---------
__ __ _
The hash table is *created* by:

    from hash_table import HashTable
    table1 = HashTable(lambda x: x%5, 5)
    '''
        Created a hash table with the
        hash function index = x%5,
        a table size of 5 and using
        linear probing as collision
        handling.
    '''

    table2 = HashTable(lambda x: x%5, 5, True)
    '''
        Created a hash table with the
        hash function index = x%5,
        a table size of 5 and using
        chaining as collision
        handling.
    '''

To *insert* a value into the table:

    table.insert("foo", 1234)
    '''
       Added the value 1234
       linked to key "foo".
    '''

A value can be *retrieved* from the hash table by:

    value = table.get("foo")
    # Got value linked to "foo".

To *remove* a value from the hash table:

    table.remove("foo")
    # Removed the entry linked to "foo".

The hash table can be *displayed* by:

    table.print_hash_table()
__ __ _