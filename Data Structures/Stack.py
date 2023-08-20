#Creating a stack
def create_stack():
    stack = []
    return stack

#Checking if stack is empty
def check_empty(stack):
    return len(stack) == 0

#Adding items into the stack
def push(stack, item):
    stack.append(item)

#Removing an element from top of stack
def pop(stack):
    if stack:
        return stack.pop()
    else:
        return "Stack is empty"

