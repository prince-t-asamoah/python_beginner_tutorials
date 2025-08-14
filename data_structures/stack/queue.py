from data_structures.queue.collection_deque import DequeQueue

class Stack(DequeQueue):
    def dequeue(self):
        return self._elements.pop()