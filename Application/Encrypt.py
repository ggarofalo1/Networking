'''
@Author: Galen Garofalo
Date: 7/24/19
Description: A list of encryption/decryption tools
'''

def caesarshiften(key, plaintext):
    """
    :return ciphertext: Encrypted text for caesar shift
    :param key: Takes in a string and counts every char to get a num for password
    :param plaintext: takes in a string of chars to be encrypted
    """
    if not key:
        key = "NO KEY"
    if not plaintext:
        plaintext = "NO TEXT ENTERED"

    ciphertext = ""
    num = 0

    list1 = list(key)  # makes an array of the password
    for i in range(len(list1)):  # goes through the array
        num += ord(list1[i])  # adds the chars together

    for i in range(len(plaintext)):  # goes through an array of plaintext
        char1 = plaintext[i]
        char1num = (ord(char1) + num) % 127 # turns the char into an int and
        # adds password to it then mods it so it is under 127 in the ascii values
        ciphertext += chr(char1num)  # adds the new char to the cipher text
    return ciphertext

def caesarshiftde(key, ciphertext):
    """
    :return plaintext: clear text for caesar shift
    :param key: key: Takes in a string and counts every char to get a num for password
    :param ciphertext: takes in a string of chars to be decrypted
    """
    if not key:
        key = "NO KEY"
    if not ciphertext:
        plaintext = "NO TEXT ENTERED"

    plaintext = ""
    num = 0

    list1 = list(key)
    for i in range(len(list1)):
        num = num + ord(list1[i])

    for i in range(len(ciphertext)):
        char1 = ord(ciphertext[i])

        check = True
        while check:
            if(char1 - num) < 0:  # if the value was moded then adds 127 to
                # start the loop when below 0
                char1 = char1 + 127
            else:
                char1num = char1 - num
                check = False

        plaintext += chr(char1num)
    return plaintext


def monoalphabeticen(key, plaintext):
    """
    :return ciphertext: Encrypted text for monoalphabetic cipher
    :param key: Takes in a string for password to be used to encrypt the plaintext
    :param plaintext: takes in a string of chars to be encrypted
    """
    ciphertext = ""

    return ciphertext


def polyalphabeticen(key, plaintext):
    """
    :return ciphertext: Encrypted text for  polyalphabetic cipher
    :param key: Takes in a string for password to be used to encrypt the plaintext
    :param plaintext: takes in a string of chars to be encrypted
    """
    ciphertext = ""

    return ciphertext


def blockcipheren(key, plaintext):
    """
    :return ciphertext: Encrypted text for block cipher
    :param key: Takes in a string for password to be used to encrypt the plaintext
    :param plaintext: takes in a string of chars to be encrypted
    """
    ciphertext = ""

    return ciphertext


def streamcipheren(key, plaintext):
    """
    :return ciphertext: Encrypted text for stream cipher
    :param key: Takes in a string for password to be used to encrypt the plaintext
    :param plaintext: takes in a string of chars to be encrypted
    """
    ciphertext = ""

    return ciphertext

cleartxt = "Hello, how are you."
password = "help"
print("MSG: " + cleartxt)
enc = caesarshiften(password, cleartxt)
print("EN MSG: "+enc)
dec = caesarshiftde(password, enc)
print("DE MSG: "+dec)
