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

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def is_empty(self):
        return True if self.head == None else False

    def length(self):
        return self.size

    def append(self, item):
        new_node = Node(item)

        if self.is_empty():
            self.head = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
        
        self.tail = new_node
        self.size += 1
    
    def prepend(self, item):
        new_node = Node(item)

        if self.is_empty():
            self.tail = new_node
        else:
            self.head.previous = new_node
            new_node.next = self.head
        
        self.head = new_node
        self.size += 1
