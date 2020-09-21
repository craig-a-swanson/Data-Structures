Answer the following questions for each of the data structures you implemented as part of this project.

## Stack

1. What is the runtime complexity of `push` using a list?
O(n) due to iterating backwards through the list

2. What is the runtime complexity of `push` using a linked list?
O(1)

3. What is the runtime complexity of `pop` using a list?
O(n) because we are removing the first element in the list and the list needs to be reindexed

4. What is the runtime complexity of `pop` using a linked list?
O(1)

5. What is the runtime complexity of `len` using a list?
O(1)

6. What is the runtime complexity of `len` using a linked list?
O(1)

## Queue

1. What is the runtime complexity of `enqueue` using a list?
O(1)

2. What is the runtime complexity of `enqueue` using a linked list?
O(1)

3. What is the runtime complexity of `dequeue` using a list?
O(n) because we are removing the first element in the list and the list needs to be reindexed

4. What is the runtime complexity of `dequeue` using a linked list?
O(1)

5. What is the runtime complexity of `len` using a list?
O(1)

6. What is the runtime complexity of `len` using a linked list?
O(1)

## Doubly Linked List

1. What is the runtime complexity of `ListNode.insert_after`?
There was not an assigned method with that name

2. What is the runtime complexity of `ListNode.insert_before`?
There was not an assigned method with that name

3. What is the runtime complexity of `ListNode.delete`?
There was not an assigned method with that name in ListNode. It was implemented in DoublyLinkedList

4. What is the runtime complexity of `DoublyLinkedList.add_to_head`?
O(1)

5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`?
O(1)

6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`?
O(1)

7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?
O(1)

8. What is the runtime complexity of `DoublyLinkedList.move_to_front`?
O(1)

9. What is the runtime complexity of `DoublyLinkedList.move_to_end`?
O(1)

10. What is the runtime complexity of `DoublyLinkedList.delete`?
We don't need to search for the node, so all of the expressions are O(1)

    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?
    Looking at search results for the array.splice() method seems to say that the worst case is O(n) since the list needs to be reindexed.  The linked list delete should be faster because the method takes a node as a parameter, accesses it directly and updates some pointers, which are all O(1).

## Binary Search Tree

1. What is the runtime complexity of `insert`? 

2. What is the runtime complexity of `contains`?

3. What is the runtime complexity of `get_max`? 

4. What is the runtime complexity of `for_each`?
    
## Heap

1. What is the runtime complexity of `_bubble_up`?

2. What is the runtime complexity of `_sift_down`?

3. What is the runtime complexity of `insert`?

4. What is the runtime complexity of `delete`?

5. What is the runtime complexity of `get_max`?
