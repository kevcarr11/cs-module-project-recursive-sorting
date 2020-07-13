# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # two iterators for traversing the two halves
    i = 0
    j = 0

    # iterator for the main list
    k = 0

    while i < len(arrA) and j < len(arrB):
        if arrA[i] < arrB[j]:
            # The value from the left half has been used
            merged_arr[k] = arrA[i]
            # Move the iterator forward
            i += 1
        else:
            merged_arr[k] = arrB[j]
            j += 1
        # Move to the next slot
        k += 1
        
    # For all the remaining values
    while i < len(arrA):
        merged_arr[k] = arrA[i]
        i += 1
        k += 1
    
    while j < len(arrB):
        merged_arr[k] = arrB[j]
        j += 1
        k += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    
    # base case
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    # Recursive call on each half
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half) 

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    return 

def merge_sort_in_place(arr, l, r):
    # Your code here
    return 

