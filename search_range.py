"""
    this function give a sorted list & a number ,
    then return range of this number in sorted list.
    
    EXAMPLE:
        input: [5, 7, 7, 8, 8, 8, 10] , number = 8
        output: [3, 5]
        ======================================================
        
"""


def search_range(arr, num):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = low + (high - low) // 2
        if num < arr[mid]:
            high = mid - 1
        elif num > arr[mid]:
            low = mid + 1
        else:
            break    
    
    for j in range(len(arr) - 1, -1, -1):
        if arr[j] == num:
            return [mid, j]
    return [None, None]


lst = [5, 7, 7, 8, 8, 8, 10]
number = 8

print(search_range(lst, number))