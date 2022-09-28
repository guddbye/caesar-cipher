import re
import string
from caesar_cipher.corpus_loader import word_list, name_list

def encrypt(code, key):
    punctuation = list(string.punctuation)
    encryptions = []

    for character in code:
        if character.isspace():
            encryptions.append(character)

        if character.isdigit():
            encryptions.append(character)

        if character in punctuation:
            encryptions.append(character)

        if character.isalpha():
            cipher = ""
            stationary_alpha = ord(character) + key

            if stationary_alpha > ord('z'):
                stationary_alpha -= 26
            last_char = chr(stationary_alpha)
            cipher += last_char
            encryptions.append(cipher)
    return ''.join([str(k) for k in encryptions])

def decrypt(code, key):
    return encrypt(code, -key)

def crack(encrypted_code):
    def char_count(char):

        possibility = char.split()
        word_count = 0
        for candidate in possibility:
            word = re.sub(r'[^A-Za-z]+', '', candidate)
            if word in word_list or word in name_list:
                word_count += 1
            else:
                pass

        return word_count

    for k in range(26):
        results = encrypt(encrypted_code, k)
        word_count = char_count(results)
        percent = int(word_count / len(results.split()) * 100)
        if percent > 90:
            return results
    return ''