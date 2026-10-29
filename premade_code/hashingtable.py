def create_hashtable(size):
    return [None]*size

def hash_function(key, size):
    return len(key) % size

def insert_into_hashtable(hashtable, key):
    index = hash_function(key, len(hashtable))
    if hashtable[index] is None:
        hashtable[index] = [key]
    else:
        hashtable[index].append(key)

def lookup_in_hashtable(hashtable, key):
    index = hash_function(key, len(hashtable))
    if hashtable[index] is not None:
        return key in hashtable[index]
    return False

size_of_hashtable = 10
my_hashtable = create_hashtable(size_of_hashtable)

insert_into_hashtable(my_hashtable,"Alice")
insert_into_hashtable(my_hashtable,"Bob")

lookup_name = "Bob"
found = lookup_in_hashtable(my_hashtable, lookup_name)
print(found)