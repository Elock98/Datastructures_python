from hash_table import HashTable

# No chaining

def my_hash_function(key):
    return sum([ord(letter) for letter in key])%10

table1 = HashTable(my_hash_function, 10)

table1.insert("foo", 100)
table1.insert("bar", "test")
table1.insert("baz", lambda x: f"value given is {x}!")

print(table1.get("foo"))
print(table1.get("baz")(600))

table1.print_hash_table()

try:
    print(table1.get("bar"))
    table1.remove("bar")
    print(table1.get("bar"))
except Exception as e:
    print(str(e))

# Chaining

table2 = HashTable(my_hash_function, 10, True)

table2.insert("foo", 100)
table2.insert("oof", 300)
table2.insert("bar", "test")
table2.insert("baz", lambda x: f"value given is {x}!")

print(table2.get("foo"))
print(table2.get("oof"))
print(table2.get("baz")(600))

table2.print_hash_table()

try:
    print(table2.get("oof"))
    table2.remove("oof")
    print(table2.get("oof"))
except Exception as e:
    print(str(e))