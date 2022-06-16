"""
    this function give a sorted list & a number ,
    then return index of this number in sorted list.
    
    EXAMPLE:
        input: [1, 3, 5, 6] , number = 3
        output: 1
        ======================================================
        input: [1, 3, 5, 6] , number = 4
        output: 2
        ======================================================
        input: [1, 3, 5, 6] , number = 7
        output: 4
        ======================================================
        input: [1, 3, 5, 6] , number = 0
        output: 0
        ======================================================
"""


def search_insert(arr, num):
    low = 0
    high = len(arr) - 1
    mid = high // 2

    while low <= high:
        if num > arr[mid]:
            mid += 1
            low = mid
        else:
            mid -= 1
            high = mid
    return low            

lst = [1, 3, 5, 6]
num = 3

print(search_insert(lst, num))