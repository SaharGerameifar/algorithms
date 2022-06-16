"""
    this function give a sorted list & a number ,
    then return index of this number in sorted list.
    
    EXAMPLE:
        input: [2, 3, 4, 6, 12, 19, 20, 21] , number = 12
        output: 5
        ======================================================
        
"""


def binary_search(arr, num):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (high + low) // 2
        val = arr[mid]
        if val == num:
            return mid
        elif val < num:
            low = mid + 1
        else:    
            high = mid - 1
    return None
    

lst = [2, 3, 4, 6, 12, 19, 20, 21]
num = 12

print(binary_search(lst, num))