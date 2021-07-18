"""
Code of the Randomized Selection algorithm (choose the i-th smallest element using a
randomly chosen pivot)

Based on the Week Four of the 'Divide and Conquer, Sorting and Searching, and Randomized
Algorithms' course on Coursera (Algorithms Specialization, Stanford University)
"""
import random
random.seed(41)

def choose_pivot_idx(arr, idx_start, idx_end, order_statistic_i):
    """
    A routine that returns an index of a pivot to use in the Randomized Selection
    algorithm when searching for "order_statistic_i"-th smallest element of the array 
    arr[idx_start : idx_end+1]

    Allows for a quick modification (pick random element, pick first element, ...),
    currently picks random pivot
    """

    return random.randint(idx_start, idx_end)

def randomized_selection(arr, idx_start, idx_end, order_statistic_i):
    """
    Implementation of the Randomized Selection algorithm 
    
    Find "order_statistic_i"-th smallest element of array arr[idx_start : idx_end+1]
    (for order_statistic_i == 1 finds the smallest element)
    
    Pivot chosen using the routine "choose_pivot_idx"

    In each recursion step, we partially sort the array such that elements smaller than
    the pivot (themselves unsorted) are to the left of the pivot and elements larger than
    the pivot (themselves unsorted) are to the right of the pivot. We then call recursion
    to only proceed with the appropriate portion of the array.
    """

    #Check bounds
    assert (idx_start >= 0 and idx_start < len(arr)), 'idx_start wrong'
    assert (idx_end >= idx_start and idx_end < len(arr)), 'idx_end wrong'

    #Terminate the recursion
    if idx_start == idx_end:
        return arr[idx_start]

    #Choose pivot and swap it to the first position
    pivot_idx = choose_pivot_idx(arr, idx_start, idx_end, order_statistic_i)
    pivot = arr[pivot_idx]
    arr[pivot_idx] = arr[idx_start]
    arr[idx_start] = pivot

    #Keep track of the split between elements smaller/larger than the pivot
    idx_first_larger_than_pivot = idx_start + 1

    #Loop over the rest of the array (pivot in the first position)
    for idx in range(idx_start+1, idx_end+1):
        #If the corresponding element is below the pivot, swap with the currently
        #left-most element larger than the pivot
        if arr[idx] < pivot:
            temp = arr[idx]
            arr[idx] = arr[idx_first_larger_than_pivot]
            arr[idx_first_larger_than_pivot] = temp
            idx_first_larger_than_pivot += 1

    #After partitioning, put pivot to the position where it belongs
    temp = arr[idx_start]
    arr[idx_start] = arr[idx_first_larger_than_pivot - 1]
    arr[idx_first_larger_than_pivot - 1] = temp

    #If pivot the number we search for, conclude, otherwise proceed with one
    #of the subarrays
    if idx_first_larger_than_pivot == idx_start + order_statistic_i:
        return pivot
    elif idx_first_larger_than_pivot < idx_start + order_statistic_i:
        return randomized_selection(
                    arr, 
                    idx_first_larger_than_pivot, 
                    idx_end,
                    order_statistic_i - idx_first_larger_than_pivot + idx_start
                )
    else:
        return randomized_selection(
                    arr, 
                    idx_start,
                    idx_first_larger_than_pivot - 1, 
                    order_statistic_i
                )

if __name__ == "__main__":
    #Test it out on a few simple examples
    for idx in range(1,8):
        arr = [5, 6, 1, 4, 7, 2, 3]
        assert(randomized_selection(arr, 0, 6, idx) == idx)

    for idx in range(1, 12):
        arr = [5, 6, 1, 4, 7, 2, 3, 8, 9, 10, 11]
        assert(randomized_selection(arr, 0, 10, idx) == idx)
