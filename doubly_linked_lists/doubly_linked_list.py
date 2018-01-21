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

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        Best case running time: Omega(1) if item is near the head of the list.
        Worst case running time: O(n) if item is near the tail of the list or
        not present and we need to loop through all n nodes in the list."""
        # Start at the head node
        node = self.head  # Constant time to assign a variable reference
        # Loop until the node is None, which is one node too far past the tail
        while node is not None:  # Up to n iterations if we don't exit early
            # Check if this node's data satisfies the given quality function
            if quality(node.data):  # Constant time to call quality function
                # We found data satisfying the quality function, so exit early
                return node  # Constant time to return data
            # Skip to the next node
            node = node.next  # Constant time to reassign a variable
        # We never found data satisfying quality, but have to return something
        return None  # Constant time to return None
        
    def delete(self, item):

        if self.is_empty():
            return None

        elif self.size == 1:
            self.head = None
            self.tail = None
            self.size = 0

        elif self.head.data == item:
            self.head = self.head.next
            self.head.previous = None
            self.size -= 1

        elif self.tail.data == item:
            self.tail = self.tail.previous
            self.tail.next = None
            self.size -= 1
        
        else: 
            node = self.find(lambda data: data == item)
            if node == None:
                return None

            node.previous = node.next
            node = None
            self.size -= 1
            