class Stack:
    #Creating a stack
    def __init__(self):
        self.stack = []

    #Checking if stack is empty
    def check_empty(self):
        return len(self.stack) == 0

    #Adding items into the stack
    def push(self, item):
        self.stack.append(item)

    #Removing an element from top of stack
    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            return "Stack is empty"
    
    def print_stack(self):
        return self.stack
