"""
Code of the Quick Sort algorithm using randomly chosen pivot

Based on the Week Three of the 'Divide and Conquer, Sorting and Searching, and Randomized
Algorithms' course on Coursera (Algorithms Specialization, Stanford University)
"""
import random
random.seed(41)

def choose_pivot_idx(arr,idx_start, idx_end):
    """
    A routine that returns a pivot to use in the Quick sort algorithm when sorting array
    "arr" between indices idx_start and idx_end

    Allows for a quick modification (pick random element, pick first element, ...)

    Currently picks random pivot
    """

    return random.randint(idx_start, idx_end)

def quicksort(arr, idx_start, idx_end):
    """
    Quick Sort implementation - example of a divide and conquer strategy

    Sort array "arr" in place between indices idx_start and idx_end (both included) using
    pivot chosen using the routine "choose_pivot_idx" and recursion

    In each recursion step, we partially sort the array such that
    elements smaller than the pivot (themselves unsorted) are to the left of the
    pivot and elements larger than the pivot (themselves unsorted) are to the right 
    of the pivot. We then call recursion to sort the subarrays.
    """

    #Check bounds
    assert (idx_start >= 0 and idx_start < len(arr)), 'idx_start wrong'
    assert (idx_end >= idx_start and idx_end < len(arr)), 'idx_end wrong'

    #Terminate the recursion
    if idx_start == idx_end:
        return

    #Choose pivot and swap it to the first position
    pivot_idx = choose_pivot_idx(arr, idx_start, idx_end)
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

    #Sort elements smaller/larger than the pivot through recursion
    #if necessary
    if idx_start <= idx_first_larger_than_pivot - 2:
        quicksort(arr, idx_start, idx_first_larger_than_pivot - 2)
    if idx_first_larger_than_pivot <= idx_end:
        quicksort(arr, idx_first_larger_than_pivot, idx_end)

    return 

if __name__ == "__main__":
    #Test it out on a few simple examples
    arr = [5, 6, 1, 4, 7, 2, 3]
    quicksort(arr, 0, 6)
    assert(arr == list(range(1, 8)))

    arr = [5, 6, 1, 4, 7, 2, 3, 8, 9, 10, 11]
    quicksort(arr, 0, 10)
    assert(arr == list(range(1, 12)))
