class Queue:
    def __init__(self):
        self.queue = []

    # Add an element
    def enqueue(self, item):
        self.queue.append(item)

    # Remove an element
    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)
        else:
            return None

    # Display  the queue
    def display(self):
        print(self.queue)

    def size(self):
        return len(self.queue)
