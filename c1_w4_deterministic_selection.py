"""
Code of the Deterministic Selection algorithm (choose the i-th smallest element using a
pivot chosen as median of medians)

Based on the Week Four of the 'Divide and Conquer, Sorting and Searching, and Randomized
Algorithms' course on Coursera (Algorithms Specialization, Stanford University)
"""

GROUP_SIZE = 5 #Size of the group used in median of medians calculation

def sort_and_get_median(arr):
    """
    Sorts an array and returns a median
    """
    arr.sort()  
    mid_idx = (len(arr)-1)//2
    return arr[mid_idx]

def median_of_medians(arr):
    """
    Splits the input array into groups of size GROUP_SIZE, calculates median in each group
    and calls the Deterministic Selection algorithm to find median of medians
    """
    if len(arr) <= GROUP_SIZE:
        return sort_and_get_median(arr)
    else:
        num_groups = len(arr)//GROUP_SIZE 
        if len(arr) % GROUP_SIZE != 0: #In case last group is smaller than GROUP_SIZE
            num_groups += 1

        medians = [
                    sort_and_get_median(arr[GROUP_SIZE * i: GROUP_SIZE * (i+1)]) 
                    for i 
                    in range(num_groups)
                  ]

        #Use recursion to get median of the medians
        return deterministic_selection(medians, 0, num_groups-1, (num_groups-1)//2)

def choose_pivot_idx(arr, idx_start, idx_end, order_statistic_i):
    """
    A routine that returns a pivot to use in the Deterministic Selection algorithm when
    searching for "order_statistic_i"-th smallest element of the array 
    arr[idx_start : idx_end+1]

    Allows for a quick modification (pick random element, pick first element, ...),
    currently picks median of medians
    """

    pivot = median_of_medians(arr[idx_start:idx_end+1])

    #We could optimize such that median of medians returns the index position as well
    for idx in range(idx_start, idx_end+1):
        if arr[idx] == pivot:
            return idx

def deterministic_selection(arr, idx_start, idx_end, order_statistic_i):
    """
    Implementation of the Deterministic Selection algorithm 
    
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
        return deterministic_selection(
                    arr, 
                    idx_first_larger_than_pivot, 
                    idx_end,
                    order_statistic_i - idx_first_larger_than_pivot + idx_start
                )
    else:
        return deterministic_selection(
                    arr, 
                    idx_start,
                    idx_first_larger_than_pivot - 1, 
                    order_statistic_i
                )

if __name__ == "__main__":
    #Test it out on a few simple examples
    for idx in range(1,8):
        arr = [5, 6, 1, 4, 7, 2, 3]
        assert(deterministic_selection(arr, 0, 6, idx) == idx)

    for idx in range(1, 12):
        arr = [5, 6, 1, 4, 7, 2, 3, 8, 9, 10, 11]
        assert(deterministic_selection(arr, 0, 10, idx) == idx)
