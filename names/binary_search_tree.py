import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack
from collections import deque

class BinarySearchTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree (recursive)
    def insert(self, value):
        # self.left or self.right can't be None to call insert()
        if value < self.value:
            # check if self.left is valid node
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchTreeNode(value)
        else: 
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTreeNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        # if target is larger than 'head' recurse on right (larger) node, or return False
        elif target > self.value:
            if self.right:
                return self.right.contains(target)
            else: return False
        # if target is smaller than 'head' recurse on left (smaller) node, or return False
        else:
            if self.left:
                return self.left.contains(target) 
            else: return False
            

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

        cb(self.value)

    # last in first out
    def depth_first_iterative_for_each(self, cb):
        stack = []
        stack.append(self)

        while len(stack) > 0:
            current_node = stack.pop()
            if current_node.right:
                stack.append(current_node.right)
            if current_node.left:
                stack.append(current_node.left)
            cb(current_node.value)

    # first in first out
    def breadth_first_iterative_for_each(self, cb):
        q = deque()
        q.append(self)

        while len(q) > 0:
            current_node = q.popleft()
            if current_node.left:
                q.append(current_node.left)
            if current_node.right:
                q.append(current_node.right)
            cb(current_node)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):

        if not node:
            return
        # on each node, check left-most bst before proceeding
        self.in_order_print(node.left)
        # once all lower values are printed, print node value
        print(node.value)
        # proceed to right/greater side values, and repeat patter
        self.in_order_print(node.right)
        

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        q = deque()
        q.append(node)
        while len(q) > 0:
            current_node = q.popleft()
            if current_node.left:
                q.append(current_node.left)
            if current_node.right:
                q.append(current_node.right)
            print(current_node.value)





    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = []
        stack.append(node)
        while len(stack) > 0:
            current_node = stack.pop()
            if current_node.left:
                stack.append(current_node.left)
            if current_node.right:
                stack.append(current_node.right)
            print(current_node.value)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        if not node:
            return
        print(node.value)
        self.pre_order_dft(node.left)
        self.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if not node:
            return
        self.post_order_dft(node.left)
        self.post_order_dft(node.right)
        print(node.value)
