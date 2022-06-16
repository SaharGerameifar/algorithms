"""
    this function give a list of prices stock ,
    then return the best time for sell stock(then sell stock with max profit).
    
    EXAMPLE:
        input: [7, 1, 5, 3, 6, 4] 
        output: 5
        ======================================================
        input: [9, 7, 6, 4, 3, 1] 
        output: 0
        
"""


def max_profit(prices):
    current_max, max_so_far = 0, 0
    for i in range(1, len(prices)):
        current_max = max(0, current_max + prices[i] - prices[i - 1])
        max_so_far = max(current_max, max_so_far)
    return max_so_far    

lst = [7, 1, 5, 3, 6, 4]

print(f'best price for sell is {max_profit(lst)}')
