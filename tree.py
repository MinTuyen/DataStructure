
import sys
from collections import deque

class Stack:
    """Stack implementation as a list"""

    def __init__(self):
        """Create a new stack"""
        self.__s = []

    def peek(self):
        """Get the value of the top item in the stack"""
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.__s[-1]

    def push(self, item):
        """Add an item to the stack"""
        self.__s.append(item)

    def pop(self):
        """Remove an item from the stack"""
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.__s.pop()

    def is_empty(self):
        """Check if the stack is empty"""
        return not self.__s

class Queue:
    """Queue implementation as a deque"""

    def __init__(self):
        """Create a new queue"""
        self.__q = deque()

    def peek(self):
        """Get the value of the front item in the queue"""
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.__q[0]

    def enqueue(self, item):
        """Add an item to the queue"""
        self.__q.append(item)

    def dequeue(self):
        """Remove an item from the queue"""
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.__q.popleft()

    def is_empty(self):
        """Check if the queue is empty"""
        return not self.__q

class Node:
    """Node class for representing a node in a binary search tree."""

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    @property
    def data(self):
        """Get the data stored in the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data stored in the node."""
        if value is None or isinstance(value, int):
            self.__data = value
        else:
            raise ValueError("data must be an int or None.")

    @property
    def left(self):
        """Get the left child of the node."""
        return self.__left

    @left.setter
    def left(self, node):
        """Set the left child of the node."""
        if node is None or isinstance(node, Node):
            self.__left = node
        else:
            raise ValueError("left must be a Node or None.")

    @property
    def right(self):
        """Get the right child of the node."""
        return self.__right

    @right.setter
    def right(self, node):
        """Set the right child of the node."""
        if node is None or isinstance(node, Node):
            self.__right = node
        else:
            raise ValueError("right must be a Node or None.")

    def get_level_helper(self, node, level, result):
        if node is None:
            return
        if level == 0:
            result.append(node.data)
        else:
            self.get_level_helper(node.left, level - 1, result)
            self.get_level_helper(node.right, level - 1, result)

class Tree:
    """Tree class for representing a binary search tree."""

    def __init__(self):
        self.root = None

    def insert(self, data):
        """Insert data into the binary search tree."""

        new_node = Node(data)

        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            parent = self.root

            while current is not None:
                parent = current

                if data < current.data:
                    current = current.left
                else:
                    current = current.right

            if data < parent.data:
                parent.left = new_node
            else:
                parent.right = new_node
    # Return True if both trees are similar. False otherwise.
    # tree is also a Tree type
    def is_similar(self, tree):
        "return True if both trees are similar"
        current =self.root
        tree_current=tree.root
        if current is None and tree_current is None:
            return True
        if current is None or tree_current is None:
            return False
        else:
            if current.data != tree_current.data:
                return False
            if current.data == tree_current.data:
                return True
            if current.left and tree_current.left:
                return current.left.is_similar(tree_current.left)
            elif current.left or tree_current.left:
                return False
            if current.right and tree_current.right:
                return current.right.is_similar(tree_current.right)
            elif current.right or tree_current.right:
                return False
            return True








    # Return a list of nodes at a given level from left to right.
    def get_level(self, level):
        'Return the list of nodes at a given level'
        if self.root is None:
            return []
        current=self.root
        result = []
        current.get_level_helper(current, level, result)  # Changed from current to self
        return result


    # Return the height of the tree
    def get_height_helper(self, node):
        'help get_height function'
        if node is None:
            return 0
        else:
            right = self.get_height_helper(node.right)
            left = self.get_height_helper(node.left)

            return max(right, left) + 1

    def get_height(self):
        'Return the height of the tree'
        current=self.root
        return self.get_height_helper(current)-1 if current else 0



    # Return the number of nodes in the tree.
    def num_nodes_helper(self,node):
        'helper function'
        if node is None:
            return 0
        else:
            right = self.num_nodes_helper(node.right)
            left = self.num_nodes_helper(node.left)

            return right+ left +1



    def num_nodes(self):
        'Return the number of nodes in the tree.'
        return self.num_nodes_helper(self.root) if self.root else 0

    # Returns the range of values stored in the tree.
    def range(self):
        'return the range'
        if self.root is None:
            return 0
        upper=self.root
        lower=self.root
        while upper.right:
            upper=upper.right
        while lower.left:
            lower=lower.left
        return upper.data-lower.data




    # Returns the list of the node that you see from left side.
    # The order of the output should be from top to down.
    def left_side_view(self):
        'left side view'
        current=self.root
        if not current:
            return []

        result = []
        queue = deque([current])

        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if i == 0:
                    result.append(node.data)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result

    # Returns the sum of the value of all leaves.
    def sum_leaf_nodes_helper(self,node):
        'helper function'
        if node is None:
            return 0
        right = node.right
        left= node.left
        if right is None and left is None:
            return node.data
        else:
            return self.sum_leaf_nodes_helper(right) + self.sum_leaf_nodes_helper(left)


    def sum_leaf_nodes(self):
        'sum all the leaf node data'
        return self.sum_leaf_nodes_helper(self.root) if self.root else 0


def main():
    """Main function. Feel free to write your own code here to test."""
    data=[]
    for i in sys.stdin:
        data.append(i.strip())
    tree1_data=data[0].split(" ")
    tree2_data=data[1].split(" ")
    tree3_data=data[2].split(" ")

    tree1=Tree()
    tree2=Tree()
    tree3=Tree()

    for i in tree1_data:
        tree1.insert(int(i))
    for i in tree2_data:
        tree2.insert(int(i))
    for i in tree3_data:
        tree3.insert(int(i))
    print(tree1_data)
    print(tree2_data)
    print(tree3_data)
    print(tree1.is_similar(tree2))
    print(tree1.is_similar(tree3))

    print(tree1.get_level(5))

    print(tree1.get_height())
    print(tree1.num_nodes())
    print(tree1.range())
    print(tree1.left_side_view())
    print(tree1.sum_leaf_nodes())
if __name__ == "__main__":
    main()
