def encrypt(string):
    """
        encodes a given string by a1z26(unicode)

        EXAMPLE:
            input: 'sahar' 
            output: [115, 97, 104, 97, 114]
    """

    return [ord(ch) for ch in string]

def decrypt(arr):
    """
        decodes a given arr by a1z26(unicode)

        EXAMPLE:
            input: [115, 97, 104, 97, 114]
            output: 'sahar'
    """

 
    return "".join(chr(elm)for elm in arr)


plain_text = 'sahar'
cipher_text = [115, 97, 104, 97, 114]

print(f'{plain_text} is plain text : {encrypt(plain_text)} is cipher text')                
print(f'{cipher_text} is cipher text : {decrypt(cipher_text)} is plain text') 

