SIZE = 6    #? when all cap, it is a constant

linked_list = [[-1, index + 1] for index in range(SIZE)]    #? this makes a 2d array with the value of the first column = -1 and the second column is 0 -> max size

linked_list[SIZE - 1][1] = -1   #? this makes the null pointer at the end
first_node = -1     #? the node list
first_empty = 0     #? index of the free list


def output_list():
    print("list:")
    current = first_node

    while current != -1:    #? use this node
        print(linked_list[current][0])
        current = linked_list[current][1]   #? load the next pointer into current

def output_freelist():
    print("freelist:")
    current = first_empty

    while current != -1:    #? use this node
        print(linked_list[current][1])
        current = linked_list[current][1]   #? load the next pointer into current

def insert_front(new_data):
    global first_node, first_empty

    if first_empty == -1:   #? check if the list is empty
        return False

    new_node = first_empty      #? take the pointer of the first empty node
    first_empty = linked_list[new_node][1]  #? change the first empty to the pointer of the node (so it points to the next one)

    linked_list[new_node][0] = new_data     #? place the new data into the new node
    linked_list[new_node][1] = first_node   #? change the pointer of the new node to the old first node
    first_node = new_node       #? update the fisrt node
    return True

def search(target):
    current = first_node

    while current != -1:
        if linked_list[current][0] == target:
            print("found")
            return current
        current = linked_list[current][1]
    print("not found")
    return -1


def insertion_sorted(new_data):     #? check whether the free list is empty, if there is no space for another node
    global first_node, first_empty
    if first_empty == -1:
        return False

    # Take the first available node from the free list
    new_node = first_empty

    # Move first_empty to the next node in the free lsit
    # This must happen before the pointer is overwritten.
    first_empty = linked_list[new_node][1]

    # Stre the new value in the allocated node
    linked_list[new_node][0] = new_data

    # Start searching from the beginning of the active list
    previous = -1
    current = first_node

    while (current != -1 and linked_list[current][0] < new_data):    #? Move throught the active list while the current value is smaller than the value being inserted
        previous = current
        current = linked_list[current][1]

    linked_list[new_node][1] = current  #? The new node points to the node that should fallow it, current will be -1 if the new node belings at the end

    if previous == -1:  #? If there is no previous node, insert at the beginning
        first_node = new_node
    else:   #? Otherwise, inser after the previous node, this handles insertion is the middle and at the end
        linked_list[previous][1] = new_node

    print("success")
    return True

def delete(target):
    global first_empty, first_node

    current = first_node
    previous = -1

    while current != -1:    #? search for the node to delete
        if linked_list[current][0] == target:
            break
        previous = current
        current = linked_list[current][1]

    if current == -1:   #? check if the node exist
        return False

    next_node = linked_list[current][1] #? storing the next node pointer

    if previous == -1:  #? if deleting the first node
        first_node = next_node
    else:   #? the previouse node now points to the next node
        linked_list[previous][1] = next_node

    linked_list[current][0] = -1    #? clearing the data in the deleted node
    linked_list[current][1] = first_empty   #? adding the deleted node to the free list
    first_empty = current   #? updating the free list pointer
    return True

insert_front(21)
output_list()
output_freelist()
delete(21)
delete(10)
output_list()
output_freelist()