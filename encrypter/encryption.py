from random import shuffle, randint
from encrypter.preparation import ascii_type, write_emojis, fetch_files, romanic_alphabet_length
from emoji import emojize
from unidecode import unidecode

# checks if txt files exist
# creates them if not
# returns dictionnary
def get_txt_files():
    txt_files = fetch_files('txt')
    if len(txt_files.keys()) == 0:
        print("No txt files")
        write_emojis('emoji.txt')
        return fetch_files('txt')
    return txt_files

def get_emoji_encryption(files: dict):
    return files['emoji']

def get_encryption(name: str, index: int = 0):
    if index > 2 or index < 0:
        return ()
    if name not in ['lowercase', 'uppercase', 'digit', 'symbol']:
        return ()
    return ascii_type[name][index]

def initialize(by: int or str, filename: str = '', index_encryption: int = 0):
    alphabet = [chr(i) for i in range(97, 123)]
    if isinstance(by, int):
        with open(filename, 'r', encoding='utf-8') as reader:
            array = reader.readlines()
            lines = [emojize(array[randint(0, len(array)-1)][:-1]) for _ in range(romanic_alphabet_length)]
    else:
        enc = get_encryption(by, index_encryption)
        items = [chr(i) for i in range(enc[0], enc[1] + 1)]
        if len(items) < romanic_alphabet_length:
            lines = items
            index = 0
            for j in range(len(items), romanic_alphabet_length):
                if index >= len(items):
                    index = 0
                lines.append(items[index] * 2)
                index += 1
        elif len(items) > romanic_alphabet_length:
            lines = [items[randint(0, len(items) - 1)] for _ in range(romanic_alphabet_length)]
        else:
            lines = items
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

def make_with_emoji(msg):
    print(f'Message: {msg}')
    files = get_txt_files()
    filename = get_emoji_encryption(files)
    encrypter = initialize(0, filename)
    return encrypt_message(encrypter, unidecode(msg))

def make_with_ascii(msg: str, type: str, index: int = 0):
    print(f'Message: {msg}')
    encrypter = initialize(type, index_encryption=index)
    return encrypt_message(encrypter, unidecode(msg))

if __name__ == '__main__':
    print(make_with_ascii('Hello', 'digit'))
    print(make_with_ascii('Today', 'uppercase'))
    print(make_with_ascii('Everyone', 'lowercase'))
    print(make_with_ascii('Month', 'symbol'))
    print(make_with_ascii('Bottle', 'symbol'), 1)
    print(make_with_ascii('Chair', 'symbol'), 2)
    print(make_with_emoji('Welcome !'))