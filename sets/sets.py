from hashtable import HashTable

# TODO: Add documentation

class Set():
    def __init__(self, elements=None):
        self.set = HashTable()
        if elements != None:
            for element in elements:
                self.add(element)

    def get_size(self):
        '''Returns size of the set'''
        return self.set.size

    def contains(self, element):
        '''Returns true or false if element in set'''
        return self.set.contains(element)

    def add(self, element):
        '''
        Method adds element to set
        Returns error if duplicate item or None
        '''
        if self.contains(element):
            raise ValueError("Cannot add duplicate element")
        self.set.set(element, element)

    def remove(self, element):
        '''
        Method removes element from set
        Returns error if element not found or None
        '''
        if self.contains(element):
            self.set.delete(element)
            return
            
        raise KeyError("Cannot remove nonexistant element")

    def union(self, other_set):
        '''
        Other_set: set
        Method joins two sets while ommitting duplicate elements
        Returns set
        '''
        if self.get_size() == 0 and other_set.get_size() == 0:
            raise ValueError('Cannot unify empty sets')

        return self.manipulate_sets('union', other_set)

    def intersection(self, other_set):
        '''
        Other_set: set
        Method creates a new set based on shared elements between two sets
        Returns set
        '''
        if self.get_size() == 0 and other_set.get_size() == 0:
            return self.set
        
        return self.manipulate_sets('intersect', other_set)

    def difference(self, other_set):
        '''
        Other_set: set
        Method creates a new set based on non shared elements between two sets
        Returns set
        '''
        if self.get_size() == 0 and other_set.get_size() == 0:
            return self.set
        
        return self.manipulate_sets('diff', other_set)

    def is_subset(self, other_set):
        '''
        Other_set: set
        Method checks if other_set is a subset of self
        Returns Boolean
        '''
        if other_set.get_size() > self.get_size():
            return False

        subset = self.manipulate_sets('intersect', other_set)

        return True if subset.get_size() == other_set.get_size() else False

    # ----------Helper function----------------
    def manipulate_sets(self, operation, set2):
        '''
        Operation: str
        Set2: set
        Method is a helper function for code reuse. Depending on the operation given it peforms a different task. 
        Returns set
        '''
        new_set = Set()
        for key, value in set2.set.items():
            if operation == 'union':
                if not self.contains(key):
                    self.add(key)

            elif operation == 'intersect':
                if self.contains(key):
                    new_set.add(key)

            elif operation == 'diff':
                if not self.contains(key):
                    new_set.add(key)

        return self if operation == 'union' else new_set

