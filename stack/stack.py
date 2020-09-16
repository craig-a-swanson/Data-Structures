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
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return self.size

    def push(self, value):
        # if the list is empty, insert at index 0 and increase the size by 1
        if self.size == 0:
            self.storage.insert(0, value)
            self.size += 1
        # if the list has values:
        #   append a 'fake' value to create the memory space
        #   do a loop starting at the end of the list
        #   set the value at that index equal to the value of the index before it
        #   when we get to index 0, set it's value to the value passed in
        #   increase the size by 1
        else:
            index = self.size
            self.storage.append(0)
            while index > 0:
                self.storage[index] = self.storage[index - 1]
                index -= 1
            self.storage[0] = value
            self.size += 1

    def pop(self):
        if self.size == 0:
            return None
        else:
            head_value = self.storage[0]
            del self.storage[0]
            self.size -= 1
            return head_value

