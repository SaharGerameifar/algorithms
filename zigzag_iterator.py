"""
    this function give two lists ,
    then return zigzag merge of two lists.
    
    EXAMPLE:
        input: [1, 3, 5, 7, 9] , [2, 4, 6, 8, 10]
        output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        
"""


class Zigzag:
    def __init__(self, list1, list2):
        self.queue = [list1, list2]

    def next(self):
        v = self.queue.pop(0) 
        r = v.pop(0)
        if v:  
            self.queue.append(v)
        return r 
    
    def has_next(self):
        if self.queue:
            return True
        return False


lst1 = [1, 3, 5, 7, 9]
lst2 = [2, 4, 6, 8, 10]
z = Zigzag(lst1, lst2)
while z.has_next():
    print(z.next(), end=' ')