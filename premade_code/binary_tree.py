SIZE = 10
DATA = 0    #? array slot for data
LEFT = 1    #? array slot for left branch
RIGHT = 2   #? array slot for right branch

tree = [[-1, -1, -1] for index in range(SIZE)]  #? each node stores data, left and right
root = -1   #? the tree has no root yet
next_free = 0   #? row 0 will be allocated first

def insert(new_data):
    global root, next_free
    if next_free >= SIZE:   #? stop if every array row is in use
        return False
    new_node = next_free    #? allocate the next unused row
    next_free += 1
    tree[new_node] = [new_data, -1, -1]
    if root == -1:  #? an empty tree uses the ne node as its root
        root = new_node
        return True
    current = root
    while True:
        if new_data < tree[current][DATA]:
            if tree[current][LEFT] == -1:
                tree[current][LEFT] = new_node
                return True
            current = tree[current][LEFT]
        else:
            if tree[current][RIGHT] == -1:
                tree[current][RIGHT] = new_node
                return True
            current = tree[current][2]

def search(target):
    global root
    current = root  #? begin at the root node
    while current != -1:
        current_data = tree[current][0]

        if target == current_data:
            print("found at index ",current)
            return current
        if target < current_data:   #? smaller targets can only be on the left side
            current_data = tree[current][LEFT]
        else:   #? larger target can only be on the right side
            current = tree[current][RIGHT]
    print("not found")
    return -1   #? the required child pointer did not exist

insert(45)
insert(25)
insert(65)
insert(15)
insert(35)
insert(55)
insert(75)
search(45)
search(1111111)
print(tree[:10])