"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_list_node = ListNode(value)
        if self.length == 0:
            self.length = 1
            self.head = new_list_node
            self.tail = new_list_node
        else:
            self.length = self.length + 1
            new_list_node.next = self.head
            self.head.prev = new_list_node
            self.head = new_list_node

        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        pass
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_list_node = ListNode(value)
        if self.length == 0:
            self.length = 1
            self.head = new_list_node
            self.tail = new_list_node
        else:
            self.length = self.length + 1
            new_list_node.prev = self.tail
            self.tail.next = new_list_node
            self.tail = new_list_node
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        pass
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        pass
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        pass

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        # if list has one node
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
        # if node = head and there are more than one nodes
        elif node == self.head:
            self.head = node.next
            node.next = None
            self.head.prev = None
            self.length -= 1
        # if node = tail
        elif node == self.tail:
            self.tail = node.prev
            node.prev = None
            self.tail.next = None
            self.length -= 1
        # otherwise
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next = None
            node.prev = None
            self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        pass

test_list = DoublyLinkedList()
test_list.add_to_head(5)
print(test_list.__len__())
test_list.add_to_head(10)
print(test_list.__len__())
print(test_list.head.next.value)
test_list.add_to_tail(20)
print(test_list.tail.value)
print(test_list.tail.prev.value)