"""
    this function give a string & a number ,
    then return rotated.
    
    EXAMPLE:
        input: hello , num = 2
        output: llohe
        ======================================================
        input: hello , num = 5
        output: hello
        ======================================================
        input: hello , num = 6
        output: elloh
        ======================================================
        input: hello , num = 7
        output: llohe
        ======================================================
"""


def rotate(s, k):
    double_s = s + s
    if k <= len(s):
        return double_s[k:k+len(s)]
    else:
        return double_s[k-len(s):k]    


string = 'hello'
k = 7
print(rotate(string, k))