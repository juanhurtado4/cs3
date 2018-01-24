from hashtable import HashTable
from helper import add_elements_from

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

        return add_elements_from(self.set, other_set)