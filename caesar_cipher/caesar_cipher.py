import sys
import string

input_file = open('mensagem.txt', 'r')

def encrypted_text(input_file):
    return input_file.read().upper()

def decrypt():
    for key in range(26):
        message = ""
        for letter in encrypted_text:
            position = ord(letter) - 65

            if position < 0 or position > 26:
                message += letter
            else:
                character = chr(((position + key) % 26) + 65)
                message += character
        print(key)
        print(message)

encrypted_text = encrypted_text(input_file)
decrypt()
