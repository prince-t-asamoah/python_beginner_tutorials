from heapq import heappush, heappop
from itertools import count
from data_structures.mixins import IterableMixin

class PriorityQueue(IterableMixin):
    def __init__(self) -> None:
        self._elements = []
        self._counter  = count()
        
    def enqueue_with_priority(self, priority, value):
        element = (-priority, next(self._counter), value) # Making the priority a negative number so that the highest one becomes the lowest
        heappush(self._elements, element) 
        
    def dequeue(self):
        return heappop(self._elements)[-1]
    
# Examples
CRITICAL = 3
IMPORTANT = 2
NEUTRAL = 1

messages = PriorityQueue()
messages.enqueue_with_priority(IMPORTANT, 'Windshield wipers turned on')
messages.enqueue_with_priority(NEUTRAL, 'Radio station tuned in')
messages.enqueue_with_priority(CRITICAL, 'Brake pedal depressed')
messages.enqueue_with_priority(IMPORTANT, 'Hazard lights turned on')

print(messages.dequeue())
print(messages.dequeue())
print(messages.dequeue())
print(messages.dequeue())
