import sys

input_string = sys.argv[1]
input_file = open(sys.argv[2], 'r')

date = input_string.replace("/", "")

def encrypted_text(input_file):
    return input_file.read()

def expanded_date(date, length):
    return (date * (int(length/len(date))+1))[:length]

def decrypt(expanded_date):
    crypt_text = ""
    for i, letter in enumerate(encrypted_text):
        if letter != " ":
            unicode_int = ord(letter) - int(expanded_date[i])
            crypt_text += chr(unicode_int)
        else:
            crypt_text += " "
    return crypt_text

encrypted_text = encrypted_text(input_file)
expanded_date = expanded_date(date, len(encrypted_text))

print(decrypt(expanded_date))
