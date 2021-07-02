"""
Code of the Merge Sort algorithm (not optimized)

Based on the Week One of the 'Divide and Conquer, Sorting and Searching, and Randomized
Algorithms' course on Coursera (Algorithms Specialization, Stanford University)
"""

def mergesort(arr):
    """
    Merge Sort implementation - example of a divide and conquer strategy
    (https://en.wikipedia.org/wiki/Merge_sort)
    """

    #Terminate the recursion
    if len(arr) < 2:
        return arr

    #Sort left and right halves of the array independently
    left_arr  = arr[:len(arr)//2]
    right_arr = arr[len(arr)//2:]

    sorted_left_arr  = mergesort(left_arr)
    sorted_right_arr = mergesort(right_arr)

    #Variables for the merge process
    result    = []
    left_idx  = 0
    right_idx = 0

    #Repeat till we run out of elements in either the left or right split
    while left_idx < len(left_arr) and right_idx < len(right_arr):
        #Append the smaller element, shift the index
        if sorted_left_arr[left_idx] <= sorted_right_arr[right_idx]:
            result.append(sorted_left_arr[left_idx])
            left_idx += 1
        else:
            result.append(sorted_right_arr[right_idx])
            right_idx += 1
    
    #Fill in the remaining elements after we are done with either left or right half
    if left_idx < len(left_arr):
        for idx in range(left_idx, len(left_arr)):
            result.append(sorted_left_arr[idx])
    elif right_idx < len(right_arr):
        for idx in range(right_idx, len(right_arr)):
            result.append(sorted_right_arr[idx])
    else:
        print('This should not happen!')
        exit()

    return result

if __name__ == "__main__":
    #Test it out on a few simple examples
    arr = [5, 6, 1, 4, 7, 2, 3]
    assert(mergesort(arr) == list(range(1, 8)))

    arr = [5, 6, 1, 4, 7, 2, 3, 8, 9, 10, 11]
    assert(mergesort(arr) == list(range(1, 12)))
