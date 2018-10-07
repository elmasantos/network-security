import sys

input_string = sys.argv[1]
input_file = open(sys.argv[2], 'r')

date = input_string.replace("/", "")

def clear_text(input_file):
    clear_text = input_file.read()
    return clear_text.lower()

def expanded_date(date, length):
    return (date * (int(length/len(date))+1))[:length]

def crypt(expanded_date):
    crypt_text = ""
    for i, letter in enumerate(clear_text):
        if letter.isalpha():
            unicode_int = ord(letter) + int(expanded_date[i])
            crypt_text += chr(unicode_int)
        else:
            crypt_text += " "
    return crypt_text

clear_text = clear_text(input_file)
expanded_date = expanded_date(date, len(clear_text))

f = open('encrypted_text.sec', 'w')
f.write(crypt(expanded_date))
f.close()
