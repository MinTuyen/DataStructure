class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack:
    def __init__(self):
        self.top = None


    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.top.data


    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node


    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        removed_data = self.top.data
        self.top = self.top.next
        return removed_data


    def is_empty(self):
        return self.top is None


my_stack = Stack()
my_stack.push(1)
my_stack.push(6)
my_stack.push(8)
my_stack.push(7)
my_stack.push(3)
my_stack.push(2)
my_stack.pop()
my_stack.push(5)
my_stack.pop()
my_stack.pop()

print(my_stack.pop() + my_stack.pop())