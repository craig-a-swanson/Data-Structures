"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""



# List version of Queue ----------------------------
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.append(value)
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return None
        else:
            head_value = self.storage[0]
            del self.storage[0]
            self.size -= 1
            return head_value

# Tests for list version of Queue()
test_queue = Queue()
test_queue.enqueue(18)
print(f'new queue: {test_queue.storage[test_queue.size - 1]}')
print(f'length is {test_queue.__len__()}')
test_queue.enqueue(99)
print(f'new queue: {test_queue.storage[test_queue.size - 1]}')
print(f'length is {test_queue.__len__()}')
test_queue.enqueue(55)
print(f'new queue: {test_queue.storage[test_queue.size - 1]}')
print(f'length is {test_queue.__len__()}')
test_queue.dequeue()
print(f'new queue: {test_queue.storage[test_queue.size - 1]}')
print(f'length is {test_queue.__len__()}')
test_queue.dequeue()
print(f'new queue: {test_queue.storage[test_queue.size - 1]}')
print(f'length is {test_queue.__len__()}')