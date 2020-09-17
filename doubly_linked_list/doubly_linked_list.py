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
        # Case of empty list
        if self.length == 0:
            return None
        # Case of one node in list
        elif self.length == 1:
            head_value = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
            return head_value
        # Case of more than one node in list
        else:
            head_value = self.head.value
            self.head = self.head.next
            self.head.prev.next = None
            self.head.prev = None
            self.length -= 1
            return head_value
            
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
        # Case of empty list
        if self.length == 0:
            return None
        # Case of one node in list
        elif self.length == 1:
            tail_value = self.tail.value
            self.head = None
            self.tail = None
            self.length -= 1
            return tail_value
        # Case of more than one node in list
        else:
            tail_value = self.tail.value
            self.tail = self.tail.prev
            self.tail.next.prev = None
            self.tail.next = None
            self.length -= 1
            return tail_value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        # change this node's previous node to point to this node's next node
        # Change this node's next node to point to this node's previous node
        # Change this node's previous to None
        # Change the current head's previous to point to this node
        # Change this node's next to the current head
        # Change the self.head to this node

        # case where this is already the head
        # case where this is the only node
        # case where this is the tail
        # case where there are more than two nodes and this is neither head nor tail
        if self.length == 1 or (node == self.head):
            pass
        elif node == self.tail:
            self.tail = node.prev
            self.tail.next = None
            self.head.prev = node
            node.next = self.head
            node.prev = None
            self.head = node
        else:
            node.prev = node.next
            node.next = node.prev
            node.prev = None
            self.head.prev = node
            node.next = self.head
            self.head = node
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        # change this node's previous node to point to this node's next node
        # Change this node's next node to point to this node's previous node
        # Change this node's next to None
        # Change the current tail's next to point to this node
        # Change this node's previous to the current tail
        # Change the self.tail to this node

        # case where this is already the tail
        # case where this is the only node
        # case where this is the head
        # case where there are more than two nodes and this is neither head nor tail
        if self.length == 1 or (node == self.tail):
            pass
        elif node == self.head:
            self.head = node.next
            self.head.prev = None
            self.tail.next = node
            node.prev = self.tail
            node.next = None
            self.tail = node
        else:
            node.prev = node.next
            node.next = node.prev
            node.next = None
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

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