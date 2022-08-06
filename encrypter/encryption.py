from random import shuffle, randint
from encrypter.preparation import write_ASCII, write_digit, write_emojis, fetch_files, romanic_alphabet_length
from emoji import emojize
from unidecode import unidecode

# checks if txt files exist
# creates them if not
# returns dictionnary
def get_txt_files():
    txt_files = fetch_files('txt')
    if len(txt_files.keys()) == 0:
        print("No txt files")
        write_ASCII('ascii.txt')
        write_emojis('emoji.txt')
        write_digit('digit.txt')
        return fetch_files('txt')
    return txt_files

# gets type of encryption, name of encryption is based on file name
# each name has an integer value associated to
# returns a dictionnary containing name matched with integer value 
def get_encryption_type(files: dict):
    types = {}
    keys = list(files.keys())

    for i in range(len(keys)):
        types[keys[i]] = i

    return types

# by choosing which type of encryption, an encryption is made
# for encryption by letter, separation by using "-" results by two character cases in list
# in case of encryption by emojis, 26 emojis are randomly picked from the file
# with encryption by digit, the lines from file are picked and each one is refactored by removing end of line
# each line of file picked is matched with alphabet letter resulting as dictionnary
# the alphabet order is randomized in purpose of giving different result
# the dictionnary is returned
def create_encryption(type: int, filename: str):
    with open(filename, 'r', encoding='utf-8') as reader:
        if type == 0:
            lines = [item[:item.index('\n')].split('-') for item in reader.readlines()]
            alphabet = [elt[1] for elt in lines]
        elif type == 1:
            lines = [item[:item.index('\n')] for item in reader.readlines()]
            alphabet = [chr(i) for i in range(97, 123)]
        elif type == 2:
            array = reader.readlines()
            lines = [emojize(array[randint(0, len(array)-1)][:-1]) for _ in range(romanic_alphabet_length)]
            alphabet = [chr(i) for i in range(97, 123)]
        else:
            return {}
    shuffle(alphabet)
    return dict(zip(alphabet, lines))

# encrypt one character by using a dictionnary
# uppercase character is treated as lowercase character
# character paramter is like a key in the dictionnary
# in case of encryption by letter, new character case is randomly selected and returned
# with emoji matching value is returned
# if character is non-alpha (letter, digit) then nothing happens and character is just returned
# if argument not in dictionnary keys, then it is returned
def encrypt_character(encryption: dict, character: str):
    if character.isupper():
        character = character.lower()
    for key, value in encryption.items():
        if character == key:
            if isinstance(value, list or tuple):
                return value[randint(0, len(value) - 1)]
            return value
        elif not character.isalnum():
            return character
    return character

# encrypt string by using a dictionnary
# empty string is return if nothing is typed
# string is treated as list and each character is encrypted, whitespace is used as separator to construct a new string as result
# the result is returned
def encrypt_message(encryption: dict, message: str):
    if len(message) == 0:
        return ''
    return " ".join([encrypt_character(encryption, character) for character in message])

def make(msg: str, encryption: int):
    files = get_txt_files()
    types = get_encryption_type(files)
    encrypter = create_encryption(types[encryption], files[encryption])
    return encrypt_message(encrypter, unidecode(msg))