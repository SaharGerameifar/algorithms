"""
    this function give a sorted list & a number ,
    then return index of this number in sorted list(last occurrence).
    
    EXAMPLE:
        input: [2, 2, 2, 3, 3, 4, 4, 5, 5, 5] , number = 4
        output: 6
        ======================================================
        
"""


def last_occurrence(arr, num):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (high + low) // 2
        if (arr[mid] == num and mid == len(arr) - 1) or \
            (arr[mid] == num and arr[mid+1] > num):
            return mid
        elif (arr[mid] <= num):
            low = mid + 1
        else:
            high = mid - 1
    return None        

lst = [2, 2, 2, 3, 3, 4, 4, 5, 5, 5]
num = 4

print(last_occurrence(lst, num))