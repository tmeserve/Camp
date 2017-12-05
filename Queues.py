class Queue(object):

    def __init__(self):
        self.make_empty()
        
    def make_empty(self):
        self._elements = []
        
    def enqueue(self, item):
        self._elements.insert(0, item)
        
    def dequeue(self):
        try:
            return self._elements.pop(0)
        except IndexError:
            return None
        
    def peek(self):
        try:
            return self._elements[0]
        except IndexError:
            return None
        
    def is_empty(self):
        return len(self._elements) == 0
    
    def is_full(self):
        return False
    
    def __len__(self):
        return len(self._elements)