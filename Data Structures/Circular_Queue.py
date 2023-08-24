class CircularQueue():
    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.head = self.tail = -1

    # Insert an element into the circular queue
    def enqueue(self, val):
        if (self.tail + 1) % self.k == self.head:
            print("The circular queue is full\n")
        elif self.head == -1:
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = val
        else:
            self.tail = (self.tail + 1) % self.k
            self.queue[self.tail] = val
    
    # Delete an element from the circular queue
    def dequeue(self):
        if self.head == -1:
            print("The circular queue is empty\n")
        elif self.head == self.tail:
            val = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return val
        else:
            val = self.queue[self.head]
            self.head = (self.head + 1) % self.k
            return val

    def printCQueue(self):
            if(self.head == -1):
                print("No element in the circular queue")

            elif (self.tail >= self.head):
                for i in range(self.head, self.tail + 1):
                    print(self.queue[i], end=" ")
                print()
            else:
                for i in range(self.head, self.k):
                    print(self.queue[i], end=" ")
                for i in range(0, self.tail + 1):
                    print(self.queue[i], end=" ")
                print()
