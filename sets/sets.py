from hashtable import HashTable

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
        if are_sets_empty(self.set, other_set):
            raise ValueError('Cannot unify empty sets')

        return manipulate_sets('union', self.set, other_set)

    def intersection(self, other_set):
        if are_sets_empty(self.set, other_set):
            return self.set
        
        return manipulate_sets()




def manipulate_sets(operation, set1, set2):

    if operation == 'union':
        for key, value in set2.set.items():
            if not set1.contains(key):
                set1.add(key, value)
        return set1

    elif operation == 'intersect':
        new_set = Set()
        for key, value in set2.set.items():
            if set1.contains(key):
                new_set.add(key, value)
        return new_set

def are_sets_empty(set1, set2):
    sets_empty = set1.get_size() == 0 and set2.get_size() == 0
    return True if sets_empty else False
