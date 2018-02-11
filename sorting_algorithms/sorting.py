def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    Running time: O(n) to check each item in the arr. O(1) if first item is not sorted, since it returns False right away.
    Memory usage: O(1) if using generators because generators do not create the entire range of indexes of items or if using a counter."""
    if len(items) == 0:
        return True
    for ind, item in enumerate(items):
        # Prevent from checking an index that is outside the range of items
        if ind + 1 == len(items):
            # items are sorted
            return True
        if item > items[ind + 1]:
            # items are not sorted
            return False

def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""

    is_sorted, last_sorted = False, len(items)
    while not is_sorted:
        is_sorted = True
        for ind, left_item in enumerate(items):
            # Prevent double checking a sorted item                
            if ind + 1 >= last_sorted:
                break

            right_item = items[ind + 1]
            # Check if not in order
            if left_item > right_item:
                is_sorted = False
                # swap items
                items[ind], items[ind + 1] = items[ind + 1], items[ind]
                
        # Update position of last sorted item to prevent double checking
        last_sorted -= 1

def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""

    for i in range(len(items)):
        small_ind = i
        for j in range(i + 1, len(items)):
            # Update index to keep track of the smallest item
            if items[j] < items[small_ind]:
                small_ind = j

        # Swap items if original index has been changed
        if small_ind != i:
            items[small_ind], items[i] = items[i], items[small_ind]

    # last_unsorted, is_sorted, ind_smallest = 0, False, 0
    # len_items = range(len(items))
    # while not is_sorted:
    #     for ind in len_items:
    #         if ind + 1 == len(items):
    #             break
    #         if items[ind_smallest] > items[ind + 1]:
    #             ind_smallest = ind + 1

    #     if last_unsorted == len(items):
    #         return

    #     curr_smallest, unsorted = items[ind_smallest], items[last_unsorted]
    #     # swap current smallest item with the first unsorted item
    #     items[ind_smallest], items[last_unsorted] = unsorted, curr_smallest


    #     last_unsorted += 1
    #     # Reset index to the first item in unsorted arr
    #     ind_smallest = last_unsorted
    #     len_items = range(last_unsorted, len(items))
    #     # Break out of loop if all items are sorted
    #     is_sorted = True if last_unsorted == len(items) else False



    


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items


def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until one list is empty
    # TODO: Find minimum item in both lists and append it to new list
    # TODO: Append remaining items in non-empty list to new list


def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half using any other sorting algorithm
    # TODO: Merge sorted halves into one list in sorted order


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if list is so small it's already sorted (base case)
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half by recursively calling merge sort
    # TODO: Merge sorted halves into one list in sorted order


def random_ints(count=20, min=1, max=50):
    """Return a list of `count` integers sampled uniformly at random from
    given range [`min`...`max`] with replacement (duplicates are allowed)."""
    import random
    return [random.randint(min, max) for _ in range(count)]


def test_sorting(sort=bubble_sort, num_items=20, max_value=50):
    """Test sorting algorithms with a small list of random items."""
    # Create a list of items randomly sampled from range [1...max_value]
    items = random_ints(num_items, 1, max_value)
    print('Initial items: {!r}'.format(items))
    print('Sorted order?  {!r}'.format(is_sorted(items)))

    # Change this sort variable to the sorting algorithm you want to test
    # sort = bubble_sort
    print('Sorting items with {}(items)'.format(sort.__name__))
    sort(items)
    print('Sorted items:  {!r}'.format(items))
    print('Sorted order?  {!r}'.format(is_sorted(items)))


def main():
    """Read command-line arguments and test sorting algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name

    if len(args) == 0:
        script = sys.argv[0]  # Get script file name
        print('Usage: {} sort num max'.format(script))
        print('Test sorting algorithm `sort` with a list of `num` integers')
        print('    randomly sampled from the range [1...`max`] (inclusive)')
        print('\nExample: {} bubble_sort 10 20'.format(script))
        print('Initial items: [3, 15, 4, 7, 20, 6, 18, 11, 9, 7]')
        print('Sorting items with bubble_sort(items)')
        print('Sorted items:  [3, 4, 6, 7, 7, 9, 11, 15, 18, 20]')
        return

    # Get sort function by name
    if len(args) >= 1:
        sort_name = args[0]
        # Terrible hack abusing globals
        if sort_name in globals():
            sort_function = globals()[sort_name]
        else:
            # Don't explode, just warn user and show list of sorting functions
            print('Sorting function {!r} does not exist'.format(sort_name))
            print('Available sorting functions:')
            for name in globals():
                if name.find('sort') >= 0:
                    print('    {}'.format(name))
            return

    # Get num_items and max_value, but don't explode if input is not an integer
    try:
        num_items = int(args[1]) if len(args) >= 2 else 20
        max_value = int(args[2]) if len(args) >= 3 else 50
        # print('Num items: {}, max value: {}'.format(num_items, max_value))
    except ValueError:
        print('Integer required for `num` and `max` command-line arguments')
        return

    # Test sort function
    test_sorting(sort_function, num_items, max_value)


if __name__ == '__main__':
    main()