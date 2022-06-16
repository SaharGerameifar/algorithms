"""
    this function give a list, then delete min element from list.
    (return min value & list with out min value.)
    
    EXAMPLE:
        input: [4, 5, 2, 8, -2, 5, 1, 9]
        output: [4, 5, 2, 8, 5, 1, 9] , -2

"""


def remove_min(lst):
    storage_lst = []
    if len(lst) == 0:
        return lst
    min = lst.pop()
    lst.append(min)
    for i in range(len(lst)):
        val = lst.pop()
        if val <= min:
            min = val
        storage_lst.append(val)

    for i in range(len(storage_lst)):
        val = storage_lst.pop()
        if val != min:
            lst.append(val)
    return lst, min                    

lst = [4, 5, 2, 8, -2, 5, 1, 9]
rm_min = remove_min(lst)
print(f"list with out min value is: {rm_min[0]} , min value is: {rm_min[1]}")

