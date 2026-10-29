front_of_queue_pointer = 0          #? mark the index of the first element
end_of_queue_pointer = -1           #? start at -1 becaise there are no elements yet
number_in_queue = 0                 #? keep track of how many items are currently in the queue
max_queue_size = 5                  #? the queue has space for 5 elements
my_queue = [None] * max_queue_size  #? create a fixed sized list of 5 slots, all initially empty

def add_to_queue(newitem):
    global end_of_queue_pointer,number_in_queue,my_queue      #? declare these variables as global
    if number_in_queue < max_queue_size:                #? prevent overflow
        end_of_queue_pointer = (end_of_queue_pointer + 1) % max_queue_size      #? move the end of pointer foward to the next available position, and wraps around to the start of the list when it reaches the end (creates circulat queue)
        my_queue[end_of_queue_pointer] = newitem
        number_in_queue += 1
    else:
        print("queue is full")

def remove_from_queue():
    global front_of_queue_pointer,end_of_queue_pointer,number_in_queue,my_queue   #? declare these variables as globa;
    if number_in_queue > 0:
        item = my_queue[front_of_queue_pointer]
        number_in_queue -=1
        if number_in_queue == 0:
            front_of_queue_pointer = 0
            end_of_queue_pointer = -1
        else:
            front_of_queue_pointer = (front_of_queue_pointer + 1) % max_queue_size
        return item
    else:
        return "stack is empty"

# Example
add_to_queue("Z")
add_to_queue("A")

print(remove_from_queue()) #! output Z
print(remove_from_queue()) #! output A