"""
    complexity O(n)

    this function give a list & min or max ,
    then return a list that have min & max.
    
    EXAMPLE:
        input: [1, 2, 3, 4, 5] , min=3
        output: [3, 4, 5]
        ======================================================
        input: [1, 2, 3, 4, 5] , max=3
        output: [1, 2, 3]
        ======================================================
        input: [1, 2, 3, 4, 5] , min=3, max=3
        output: [3]

"""


def limit(arr, min=None, max=None):
    min_check = lambda val: True if min is None else (val >= min)
    max_check = lambda val: True if max is None else (val <= max)
    return [val for val in arr if min_check(val) and max_check(val)]

lst = [1, 2, 3, 4, 5]

print(limit(lst, min=3))
print(limit(lst, max=3))
print(limit(lst, min=3, max=3))

