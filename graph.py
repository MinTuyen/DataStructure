#  Name 1:
#  EID 1:

#  Name 2:
#  EID 2:

import os
import sys
from collections import deque

# -----------------------PRINTING LOGIC, DON'T WORRY ABOUT THIS PART----------------------------
os.system("")  # Enables printing colors on Windows
RESET_CHAR = "\u001b[0m"  # Code to reset the terminal color
COLOR_DICT = {
    "black": "\u001b[30m",
    "red": "\u001b[31m",
    "green": "\u001b[32m",
    "yellow": "\u001b[33m",
    "blue": "\u001b[34m",
    "magenta": "\u001b[35m",
    "cyan": "\u001b[36m",
    "white": "\u001b[37m"
}
BLOCK_CHAR = "\u2588"  # Character code for a block

def colored(text, color):
    """Wrap the string with the color code."""
    color = color.strip().lower()
    if color not in COLOR_DICT:
        raise ValueError(color + " is not a valid color!")
    return COLOR_DICT[color] + text

def print_block(color):
    """Print a block in the specified color."""
    print(colored(BLOCK_CHAR, color) * 2, end='')
# -----------------------PRINTING LOGIC, DON'T WORRY ABOUT THIS PART----------------------------

class Stack:
    """Stack implementation as a list"""

    def __init__(self):
        """Create new stack"""
        self.items = []

    def peek(self):
        """Get the value of the top item in the stack"""
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.items[-1]

    def push(self, item):
        """Add an item to the stack"""
        self.items.append(item)

    def pop(self):
        """Remove an item from the stack"""
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.items.pop()

    def is_empty(self):
        """Check if the stack is empty"""
        return not self.items

class Queue:
    """Queue class for search algorithms."""
    def __init__(self):
        self.q = deque()

    def peek(self):
        """Get the front element of the queue."""
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.q[0]

    def enqueue(self, item):
        """Add an item to the end of the queue."""
        self.q.append(item)

    def dequeue(self):
        """Remove and return the front element of the queue."""
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.q.popleft()

    def is_empty(self):
        """Check if the queue is empty."""
        return not self.q

class ColoredVertex:
    """Class for a graph vertex."""
    def __init__(self, index, x, y, color):
        self.index = index
        self.color = color
        self.prev_color = color
        self.x = x
        self.y = y
        self.edges = []
        self.visited = False

    def add_edge(self, vertex_index):
        """Add an edge to another vertex."""
        self.edges.append(vertex_index)

    def visit_and_set_color(self, color):
        """Set the color of the vertex and mark it visited."""
        self.visited = True
        self.prev_color = self.color
        self.color = color
        print("Visited vertex " + str(self.index))

    def __str__(self):
        return f"index: {self.index}, color: {self.color}, x: {self.x}, y: {self.y}"

class ImageGraph:
    """Class for the graph."""
    def __init__(self, image_size):
        self.vertices = []
        self.image_size = image_size

    def print_image(self):
        """Print the image formed by the vertices."""
        img = [["black" for _ in range(self.image_size)] for _ in range(self.image_size)]

        # Fill img array
        for vertex in self.vertices:
            img[vertex.y][vertex.x] = vertex.color

        for line in img:
            for pixel in line:
                print_block(pixel)
            print()
        # Print new line/reset color
        print(RESET_CHAR)

    def reset_visited(self):
        """Reset the visited flag for all vertices."""
        for vertex in self.vertices:
            vertex.visited = False

    # Print the adjacency matrix.
    # Don't remove the first print statement we provide
    # after all printing logic is done, add a final print() before method ends
    def print_adjacency_matrix(self):

        print("Adjacency matrix:")

        # Add code below
        raise NotImplementedError("Remove this exception and print the adjacency matrix here.")


    # Perform Breadth-First Search algorithm
    # Don't remove the first 2 statements we provide
    # you may choose to call print_images in this method for debugging yourself
    def bfs(self, start_index, color):

        self.reset_visited()
        print("Starting BFS; initial state:")
        self.print_image()

        # Add code below
        queue=Queue()
        queue.enqueue(start_index)
        while queue.is_empty():
            current_index = queue.dequeue()
            current_vertex=self.vertices[current_index]
            if not current_vertex.visited:
    
                current_vertex.visited = True
                current_vertex.color = color
                for neighbor_index in current_vertex.edges:
                    neighbor = self.vertices[neighbor_index]
                    if not neighbor.visited:

                        queue.enqueue(neighbor_index)
        self.print_image()

    # Perform Depth-First Search algorithm.
    # Don't remove the first 2 statements we provide.
    # you may choose to call print_images in this func method debugging yourself
    def dfs(self, start_index, color):
        self.reset_visited()
        print("Starting DFS; initial state:")


        # Add code below
        stack=Stack()
        stack.push(start_index)
        while stack.is_empty():
            current_index=stack.pop()
            current_vertex= self.vertices[current_index]
            if not current_vertex.visited:
                current_vertex.visited = True
                current_vertex.color= color

                for neighbor_index in current_vertex.edges:
                    neighbor = self.vertices[neighbor_index]
                    if not neighbor.visited:
                        stack.push(neighbor_index)

        self.print_image()
# Create the graph from input data.
def create_graph(data):

    # split the data by new line

    # get size of image and number of vertices

    # create the ImageGraph

    # create vertices - vertex info has the format "x,y,color"

    # create edges between vertices - edge info has the format "from_index,to_index"
    # connect vertex A to vertex B and the other way around

    # read search starting position and color

    # return the ImageGraph, starting position, and color as a tuple in this order.
    raise NotImplementedError("Remove this exception and implement create_graph here.")

def main():

    # read input
    data = sys.stdin.read()

    # create graph, passing in data

    # call print adjacency matrix

    # run bfs

    # reset by creating graph again

    # run dfs


if __name__ == "__main__":
    main()
