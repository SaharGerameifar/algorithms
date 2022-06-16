"""
    this function give two string(s,t) ,
    then return true if strings are isomorphic.
    
    EXAMPLE:
        input: s = foo , t = bar
        output: False
        ======================================================
        input: s = foo , t = bee
        output: True
        
"""


def is_isomorphic(s, t):
    if len(s) != len(t):
        return False

    dict = {}
    set_values = set()
    for i in range(len(s)):
        if s[i] not in dict:
            if t[i] in set_values:
                return False
            dict[s[i]] = t[i]
            set_values.add(t[i]) 
        else: 
            if dict[s[i]] != t[i]:
                return False
    return True                            

s = 'foo'
t = 'bee'

print(is_isomorphic(s, t))