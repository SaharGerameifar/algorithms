"""
    this function give a numbers list, then sort them.
    
    EXAMPLE:
        input: [64, 1, 25, 67, 98, 17]
        output: [1, 17, 25, 64, 67, 98]

"""


def bead_sort(numbers_list):
    if any(not isinstance(x, int) or x < 0 for x in numbers_list):
        raise TypeError('numbers list must be list of non-negative integers.')

    for _ in range(len(numbers_list)):
        for i, (rod_upper, rod_lower) in enumerate(zip(numbers_list, numbers_list[1:])):
            if rod_upper > rod_lower:
                numbers_list[i] -= rod_upper - rod_lower  
                numbers_list[i + 1] += rod_upper - rod_lower
    return numbers_list 

nums = [64, 1, 25, 67, 98, 17]
print(bead_sort(nums))

