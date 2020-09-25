"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

# List version of Stack ------------------------
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return self.size

#     def push(self, value):
#         # if the list is empty, insert at index 0 and increase the size by 1
#         if self.size == 0:
#             self.storage.insert(0, value)
#             self.size += 1
#         # if the list has values:
#         #   append a 'fake' value to create the memory space
#         #   do a loop starting at the end of the list
#         #   set the value at that index equal to the value of the index before it
#         #   when we get to index 0, set it's value to the value passed in
#         #   increase the size by 1
#         else:
#             index = self.size
#             self.storage.append(0)
#             while index > 0:
#                 self.storage[index] = self.storage[index - 1]
#                 index -= 1
#             self.storage[0] = value
#             self.size += 1

#     def pop(self):
#         if self.size == 0:
#             return None
#         else:
#             head_value = self.storage[0]
#             del self.storage[0]
#             self.size -= 1
#             return head_value

# Linked list version of Stack ----------------------------
class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None # Stores a node that corresponds to our first node in the list
        self.tail = None # Stores a node that is the end of the list

    def add_to_head(self, value):
        # create a node to add
        new_node = Node(value)
        # check if list is empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            # new_node should point to current head
            new_node.next_node = self.head
            # move head to new node
            self.head = new_node

    def add_to_tail(self, value):
        # create a node to add
        new_node = Node(value)
        # check if list is empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            # point the node at the current tail to the new_node
            self.tail.next_node = new_node
            self.tail = new_node

    # remove the head and return its value
    def remove_head(self):
        # if list is empty, do nothing
        if not self.head:
            return None
        # if list only has one element, set head and tail to None
        if self.head.next_node is None:
            head_value = self.head.value
            self.head = None
            self.tail = None
            return head_value
        # otherwise we have more elements in the list
        head_value = self.head.value
        self.head = self.head.next_node
        return head_value

    def contains(self, value):
        if self.head is None:
            return False
        
        # Loop through each node until we see the value or cannot go further
        current_node = self.head

        while current_node is not None:
            # check if this is the node we are looking for
            if current_node.value == value:
                return True
            
            # otherwise, go to the next node
            current_node = current_node.next_node
        return False

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.add_to_head(value)
        self.size += 1

    def pop(self):
        pop_result = self.storage.remove_head()
        if pop_result is not None:
            self.size -= 1
        return pop_result