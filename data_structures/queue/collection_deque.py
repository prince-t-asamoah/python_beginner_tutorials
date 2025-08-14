from collections import deque
from data_structures.mixins import IterableMixin

class DequeQueue(IterableMixin):
    def __init__(self, *elements):
        self._elements = deque(elements)
        
    def enqueue(self, element):
        self._elements.append(element)
        
    def dequeue(self):
        return self._elements.popleft()
    
    def __iter__(self):
        while len(self._elements) > 0:
            yield self.dequeue()
            
    def __len__(self):
        return len(self._elements)
