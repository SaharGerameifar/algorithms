import random


class OneTimePad:
    def encrypt(self, plaintext):
        """
            encodes a given string by ONE TIME PAD 

            EXAMPLE:
                input: 'sahar' 
                output: cipher = [27144, 6578, 86697, 57918, 1107], key = [117, 46, 247, 197, 9] 
        """

        plain = [ord(i) for i in plaintext]
        key, cipher = [], []
        for i in plain:
            k = random.randint(1, 300)
            c = (i + k) * k 
            cipher.append(c)
            key.append(k)
        return cipher, key  

    def decrypt(self, ciphertext, key):
        """
            decodes a given string by ONE TIME PAD 

            EXAMPLE:
                input: cipher = [27144, 6578, 86697, 57918, 1107], key = [117, 46, 247, 197, 9] 
                output: 'sahar'
        """

        plain = []
        for i in range(len(key)):
            p = int((ciphertext[i] - key[i] ** 2) / key[i])
            plain.append(chr(p))
        return "".join([i for i in plain])  


plaintext = 'sahar'
ciphertext, key = OneTimePad().encrypt(plaintext)
print(f'{plaintext} is plain text: {ciphertext} is cipher text and {key} is key.')
plaintext = OneTimePad().decrypt(ciphertext, key)
print(f'{ciphertext} is cipher text and {key} is key: {plaintext} is plain text.')                

               