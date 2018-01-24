from hashtable import HashTable

# TODO: Add documentation

class Set():
    def __init__(self, elements=None):
        self.set = HashTable()
        if elements != None:
            for element in elements:
                self.add(element)

    def get_size(self):
        return self.set.size

    def contains(self, element):
        return self.set.contains(element)

    def add(self, element):
        if self.contains(element):
            raise ValueError("Cannot add duplicate element")
        self.set.set(element, element)

    def remove(self, element):
        if self.contains(element):
            self.set.delete(element)
            return
            
        raise KeyError("Cannot remove nonexistant element")

    def union(self, other_set):
        if self.get_size() == 0 and other_set.get_size() == 0:
            raise ValueError('Cannot unify empty sets')

        return self.manipulate_sets('union', other_set)

    def intersection(self, other_set):
        if self.get_size() == 0 and other_set.get_size() == 0:
            return self.set
        
        return self.manipulate_sets('intersect', other_set)

    def difference(self, other_set):
        if self.get_size() == 0 and other_set.get_size() == 0:
            return self.set
        
        return self.manipulate_sets('diff', other_set)

    def is_subset(self, other_set):
        if other_set.get_size() > self.get_size():
            return False
        subset = self.manipulate_sets('intersect', other_set)

        return True if subset.get_size() == other_set.get_size() else False

    def manipulate_sets(self, operation, set2):

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

