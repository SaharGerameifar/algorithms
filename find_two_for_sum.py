"""
    this function give a numbers list and a target,
    then find two numbers in list that sum of them is equle target.
    (return index of two numbers in list)
    
    EXAMPLE:
        input: [2, 7, 11, 15] , target = 18
        output: [1, 2]

"""


def find_two_for_sum(lst, target):
    p1, p2 = 0, len(lst) - 1
    while p1 < p2:
        s = lst[p1] + lst[p2]
        if s == target:
            return [p1, p2]
        elif s > target:
            p2 = p2 - 1
        else:
            p1 = p1 + 1        


lst = [2, 7, 11, 15]
target = 18
print(find_two_for_sum(lst, target))

