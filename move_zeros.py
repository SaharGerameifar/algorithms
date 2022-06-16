"""
    this function give a list, then move zeros at the end of list.
    
    EXAMPLE:
        input: [False, 1, 0, 1, 2, 0, 1, 3, "a"]
        output: [False, 1, 1, 2, 1, 3, 'a', 0, 0]

"""


def move_zeros(lst):
    result = []
    count_zeros = 0
    for i in lst:
        if i == 0 and type(i) != bool:
            count_zeros += 1
        else:
            result.append(i)
    result.extend([0] * count_zeros)            
    return result

lst = [False, 1, 0, 1, 2, 0, 1, 3, "a"]
print(move_zeros(lst))

