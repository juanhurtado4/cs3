class Node():
    def __init__(self, item):
        self.previous = None
        self.next = None
        self.data = item

class Linked_list():
    
    def __init__(self, items=None):
        self.head = None
        self.tail = None
        self.size = 0
        if items != None:
            for item in items:
                self.append(item)