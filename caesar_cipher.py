from string import ascii_letters


def encrypt(string, k):
    """
        encodes a given string by CAESAR CIPHER

        EXAMPLE:
            input: 'sahar' , k=3
            output: 'vdkdu'
    """

    alpha = ascii_letters
    result = ''

    for ch in string:
        if ch not in alpha:
            result += ch
        else:
            new_k = (alpha.index(ch) + k) % len(alpha)
            result += alpha[new_k]
    return result

def decrypt(string, k):
    """
        decodes a given string by CAESAR CIPHER

        EXAMPLE:
            input: 'vdkdu' , k=3
            output: 'sahar'
    """

    k *= -1
    return encrypt(string, k)

def brute_force(string):
    """return all the possible combinations of k and decoded string

    """

    alpha = ascii_letters
    k = 1
    result = ''
    brute_force_data = {}

    while k <= len(alpha):
        result = decrypt(string, k)
        brute_force_data[k] = result
        result = ''
        k += 1
    return brute_force_data


plain_text = 'sahar'
cipher_text = 'vdkdu'
k = 3
print(f'{plain_text} is plain text and {k} is key: {encrypt(plain_text, k)} is cipher text')                
print(f'{cipher_text} is cipher text and {k} is key: {decrypt(cipher_text, k)} is plain text') 
print(f'brute force data for this cipher text {cipher_text} is:')
print(brute_force(cipher_text))
