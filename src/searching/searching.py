# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # base case
    if end < start:
        return -1

    mid_index = (start + end) // 2

    # base case
    if target == arr[mid_index] :
        return mid_index
        # decrement end value and recurse 
    elif target < arr[mid_index]:
        return binary_search(arr, target, start, mid_index -1)
        # increment start value and recurse
    elif target > arr[mid_index]:
        return binary_search(arr, target, mid_index +1, end)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    pass

