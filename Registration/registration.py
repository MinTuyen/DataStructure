# Name 1: Hoang Minh Nguyen
# EID 1:

# Name 2:
# EID 2:

import sys
from collections import deque

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

    def __str__(self):
        """String representation of the stack"""
        return str(self.items)

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

    def __str__(self):
        """String representation of the queue"""
        return str(self.q)

class Vertex:
    """Vertex Class using properties and setters for better encapsulation."""

    def __init__(self, label):
        self.__label = label
        self.visited = False

    @property
    def visited(self):
        """Property to get the visited status of the vertex."""
        return self.__visited

    @visited.setter
    def visited(self, value):
        """Setter to set the visited status of the vertex."""
        if isinstance(value, bool):
            self.__visited = value
        else:
            raise ValueError("Visited status must be a boolean value.")

    @property
    def label(self):
        """Property to get the label of the vertex."""
        return self.__label

    def __str__(self):
        """String representation of the vertex"""
        return str(self.__label)


class Graph:
    """A Class to present Graph."""

    def __init__(self):
        self.vertices = []  # a list of vertex objects
        self.adjacency_matrix = []  # adjacency matrix of edges

    def has_vertex(self, label):
        """Check if a vertex is already in the graph"""
        num_vertices = len(self.vertices)
        for i in range(num_vertices):
            if label == self.vertices[i].label:
                return True
        return False

    def get_index(self, label):
        """Given a label get the index of a vertex"""
        num_vertices = len(self.vertices)

        for i in range(num_vertices):
            if label == self.vertices[i].label:
                return i
        return -1

    def add_vertex(self, label):
        """Add a Vertex with a given label to the graph"""
        if self.has_vertex(label):
            return

        # add vertex to the list of vertices
        self.vertices.append(Vertex(label))

        # add a new column in the adjacency matrix
        num_vertices = len(self.vertices)
        for i in range(num_vertices - 1):
            self.adjacency_matrix[i].append(0)

        # add a new row for the new vertex
        new_row = []
        for i in range(num_vertices):
            new_row.append(0)
        self.adjacency_matrix.append(new_row)

    def add_edge(self, start, finish):
        """Add unweighted directed edge to graph"""
        self.adjacency_matrix[start][finish] = 1

    def get_adjacent_vertices(self, vertex_index):
        """Return adjacent vertex indices to vertex_index"""
        vertices = []
        num_vertices = len(self.vertices)
        for j in range(num_vertices):
            if self.adjacency_matrix[vertex_index][j]:
                vertices.append(j)
        return vertices

    # Determine whether or no the graph has a cycle
    # Return as a boolean value
    def has_cycle(self):
        """Use DFS"""
        def dfs(vertex_index, visited, stack):
            visited[vertex_index] = True
            stack[vertex_index] = True

            for adjacent_index in self.get_adjacent_vertices(vertex_index):
                if not visited[adjacent_index]:
                    if dfs(adjacent_index, visited, stack):
                        return True
                elif stack[adjacent_index]:
                    return True

            stack[vertex_index] = False
            return False

        visited = [False] * len(self.vertices)
        stack = [False] * len(self.vertices)

        for vertex_index in range(len(self.vertices)):
            if not visited[vertex_index]:
                if dfs(vertex_index, visited, stack):
                    return True
        return False

    # Return a valid ordering of courses to take for registration as a list of vertex labels.
    # This method assumes that there is a valid registration plan.
    def get_registration_plan(self):

        # Because we don't want to destroy the original graph,
        # we have defined helper functions that work with a copy of the
        # adjacency matrix and vertices. This is also a hint that we
        # suggest you to manipulate the graph copy to solve this method.

        # We encourage you to use these variables and functions, although
        # if you come up with a solution that doesn't, you may delete them.

        # Temporary copy of in-degrees to maintain the integrity of the original graph
        in_degree = [0] * len(self.vertices)
        for i in range(len(self.vertices)):
            for j in range(len(self.vertices)):
                if self.adjacency_matrix[i][j] == 1:
                    in_degree[j] += 1

        # Queue to hold all vertices with no incoming edge
        queue = []
        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                queue.append(i)

        courses = []
        while queue:
            vertex_index = queue.pop(0)
            courses.append(self.vertices[vertex_index].label)  # Append vertex label to the sorted order

            # Reduce the in-degree for each adjacent vertex
            for i in range(len(self.vertices)):
                if self.adjacency_matrix[vertex_index][i] == 1:
                    in_degree[i] -= 1
                    if in_degree[i] == 0:
                        queue.append(i)  # If in-degree becomes zero, add it to the queue

        # Check if there was a cycle, which shouldn't happen as we assume the graph is acyclic
        if len(courses) != len(self.vertices):
            return []  # This case should not occur because we assume a valid plan exists
        return courses

# Read the input file and construct the graph. The output code has been written for you.
def main():
    # create a Graph object
    graph = Graph()
    data_input = sys.stdin.read
    data = data_input().splitlines()

    # Read the number of vertices
    num_vertices = int(data[0])

    # Read the vertices and add them into the graph
    index = 1
    for _ in range(num_vertices):
        vertex_label = data[index]
        graph.add_vertex(vertex_label)
        index += 1

    # Read the number of edges
    num_edges = int(data[index])
    index += 1

    # Read the vertices and add them into the graph
    index = 1
    for _ in range(num_vertices):
        vertex_label = data[index]
        graph.add_vertex(vertex_label)
        index += 1

    # Read the number of edges
    num_edges = int(data[index])
    index += 1

    # Read the edges and insert them into the graph
    for _ in range(num_edges):
        edge = data[index].split()
        start_label = edge[0]
        end_label = edge[1]
        start_index = graph.get_index(start_label)
        finish_index = graph.get_index(end_label)
        graph.add_edge(start_index, finish_index)
        index += 1
    ####################################################################################
    # DO NOT CHANGE ANYTHING BELOW THIS
    if graph.has_cycle():
        print("Registration plan invalid because a cycle was detected.")
    else:
        print("Valid registration plan detected.")

        courses = graph.get_registration_plan()
        print()
        print("Registration plan: ")
        print(courses)

main()
