class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.items = [None] * size
        self.front = -1
        self.rear = -1

    def isEmpty(self):
        return self.front == -1

    def isFull(self):
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, value):

        # Queue Full
        if self.isFull():
            print("Queue is full")

        # First Element
        elif self.isEmpty():
            self.front = 0
            self.rear = 0
            self.items[self.rear] = value

        # Normal Insert
        else:
            self.rear = (self.rear + 1) % self.size
            self.items[self.rear] = value

    def dequeue(self):

        # Queue Empty
        if self.isEmpty():
            print("Queue is empty")

        # Single Element
        elif self.front == self.rear:
            temp = self.items[self.front]
            self.items[self.front] = None
            self.front = -1
            self.rear = -1
            return temp

        # Normal Delete
        else:
            temp = self.items[self.front]
            self.items[self.front] = None
            self.front = (self.front + 1) % self.size
            return temp