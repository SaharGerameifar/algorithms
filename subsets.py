from itertools import chain, combinations

"""
    complexity O(n^n)

    this function give a iterable object,
    then return all combinations of elements in iterable object.
    (All subsets of a set)
    
    EXAMPLE:
        input: ('a', 'b', 'c')
        output: [(), ('a',), ('b',), ('c',), ('a', 'b'), ('a', 'c'), ('b', 'c'), ('a', 'b', 'c')]

"""


def subsets(iterable):
    s = list(iterable)
    return list(chain.from_iterable(combinations(s,r) for r in range(len(s) + 1)))


lst = ('a', 'b', 'c')
print(subsets(lst))

