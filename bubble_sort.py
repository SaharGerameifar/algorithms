"""
    complexity O(n^2)

    this function give a numbers list, then sort them.
    
    EXAMPLE:
        input: [64, 1, 25, 67, 98, 17]
        output: [1, 17, 25, 64, 67, 98]

"""


def bubble_sort(numbers_list):
    length = len(numbers_list)
    for i in range(length - 1):
        swapped = False
        for j in range(length - 1 - i):
            if numbers_list[j] > numbers_list[j + 1]:
                swapped = True
                numbers_list[j], numbers_list[j + 1] = numbers_list[j + 1], numbers_list[j]
        if not swapped:
            break
    return numbers_list


nums = [64, 1, 25, 67, 98, 17]
print(bubble_sort(nums))

