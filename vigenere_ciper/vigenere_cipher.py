import sys

input_file = open('musica.sec', 'r')
key = 'despacito'
alphabet = " !#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"

def encrypted_text(input_file):
    return input_file.read()

def expanded_key(key, length):
    return (key * (int(length/len(key))+1))[:length]

def decrypt(expanded_key):
    decrypted_text = ""
    for i, letter in enumerate(encrypted_text):
        if letter in alphabet:
            c = alphabet.index(letter)
            k = alphabet.index(expanded_key[i])
            unicode_int = (c - k) % 94

            decrypted_text += alphabet[unicode_int]
        else:
            decrypted_text += letter
    print(decrypted_text)

encrypted_text = encrypted_text(input_file)
expanded_key = expanded_key(key, len(encrypted_text))

decrypt(expanded_key)
