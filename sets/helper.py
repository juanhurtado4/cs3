def add_elements_from(set1, set2):
    for key, value in set2.set.items():
        if not set1.contains(key):
            set1.set(key, value)
    return set1
    

    