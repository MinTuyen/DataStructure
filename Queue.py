class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

 

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

 

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.front.data

 

    def enqueue(self, item):
        new_node = Node(item)
        if self.rear:
            self.rear.next = new_node
        self.rear = new_node
        if not self.front:
            self.front = self.rear

 

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        removed_data = self.front.data
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return removed_data

 

    def is_empty(self):
        return self.front is None
    

 

my_queue = Queue()
my_queue.enqueue(1)
my_queue.enqueue(6)
my_queue.enqueue(8)
my_queue.enqueue(7)
my_queue.enqueue(3)
my_queue.enqueue(2)
my_queue.dequeue()
my_queue.enqueue(5)
my_queue.dequeue()
my_queue.dequeue()

 

print(my_queue.dequeue() + my_queue.dequeue())