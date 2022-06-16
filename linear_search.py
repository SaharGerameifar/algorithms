"""
    this function give a list & a number ,
    then return index of this number in list.
    
    EXAMPLE:
        input: [1, 2, 5, 8, 11, 14, 18, 23, 32, 48] , number = 11
        output: 4
        ======================================================
        
"""


def linear_search(arr, num):
    for i in range(len(arr)):
        if arr[i] == num:
            return i
    return None


lst = [1, 2, 5, 8, 11, 14, 18, 23, 32, 48]
num = 11

print(linear_search(lst, num))