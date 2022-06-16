"""
    complexity O(n)

    this function give a list ,
    then return most frequent values.
    
    EXAMPLE:
        input: [1, 2, 1, 3, 4, 2]
        output: [1, 2]
       
"""


def top_1(arr):
    values = {}
    result = []
    max_frequent_val = 0

    for i in arr:
        if i in values:
            values[i] += 1
        else:
            values[i] = 1

    max_frequent_val = max(values.values())

    for i in values.keys():
        if values[i] == max_frequent_val:
            result.append(i)
        else:
            continue 
    return result       



lst = [1, 2, 1, 3, 4, 2]

print(top_1(lst))


