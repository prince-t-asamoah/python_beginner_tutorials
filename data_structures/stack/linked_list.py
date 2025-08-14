from data_structures.mixins import Node

class Stack:
    def __init__(self) -> None:
        self.head = Node('head')
        self.size = 0
        
    def __str__(self):
        current = self.head.next
        out = ""
        
        while current:
            out += str(current.value) + " ->"
            current = current.next
        return out[:-2]
    
    # Get current size of stack
    def get_size(self):
        return self.size
    
    # Check if stack is empty
    def is_empty(self):
        return self.size == 0

    # Get the top item of the stack
    def peek(self):
        if self.is_empty():
            return None
        if self.head.next:
            return self.head.next.value
        return None
    
    # Push a value into a stack
    def push(self, value):
        node = Node(value)
        node.next = self.head.next # The new node points to the current head
        self.head.next = node
        self.size += 1
        
    # Remove a value from the stack and return
    def pop(self):
        try:
            if self.is_empty():
                raise Exception("Popping from an empty stack")
            node_to_be_removed = self.head.next
            if node_to_be_removed:
                self.head.next = node_to_be_removed.next
                self.size -= 1
                return node_to_be_removed.value
            return None
        except Exception as error:
            print(error)
    