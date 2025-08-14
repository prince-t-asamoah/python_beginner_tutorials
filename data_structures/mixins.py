class IterableMixin:
    def __len__(self):
        return len(self._elements) # type: ignore
    
    def __iter__(self):
        while len(self) > 0:
            yield self.dequeue() # type: ignore
            
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None  # type: Node | None
        