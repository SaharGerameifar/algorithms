"""
    this function give a sorted list & a number ,
    then return index of this number in sorted list(first occurrence).
    
    EXAMPLE:
        input: [2, 2, 2, 3, 3, 4, 4, 5, 5, 5] , number = 4
        output: 5
        ======================================================
        
"""


def first_occurrence(arr, num):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (high + low) // 2
        if low == high:
            break
        if arr[mid] < num:
            low = mid + 1
        else:    
            high = mid 
    if arr[low] == num:
        return low        
    return None
    

lst = [2, 2, 2, 3, 3, 4, 4, 5, 5, 5]
num = 4

print(first_occurrence(lst, num))