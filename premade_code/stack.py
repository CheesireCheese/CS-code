base_of_stack = 0                               #? Marks the bottom of the stack 
top_of_stack = -1                               #? Indicate the stack is empty
max_stack_size = 5                              #? The maximum capacity of the stack

my_stack = [None] * max_stack_size              #? create a list of 5 empty slots --> will not return an error

def push(newitem):
    global top_of_stack, my_stack               #? Declare these varaibles as global
    if top_of_stack == max_stack_size - 1:      #? check if there are any space left, prevent overflow
        top_of_stack +=1                        #? increasing the top according to new added value
        my_stack[top_of_stack] = newitem        #? add the new item

def pop():
    global top_of_stack, my_stack               #? Declare these varaibles as global
    if top_of_stack >-1:                        #? Check if there's anything, preventing underflow
        item = my_stack[top_of_stack]           #? retrieve current top item
        top_of_stack -= 1                       #? Pointer down one position
        return item                             #? sends back the item that was popped so u can use

push("A")
push("B")
push("C")

print(pop()) # Output: C
print(pop()) # Output: B
print(pop()) # Output: A