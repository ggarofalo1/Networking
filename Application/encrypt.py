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

    ciphertext = ""
    num = 0

    list1 = list(key)  # makes an array of the password
    for i in range(len(list1)):  # goes through the array
        num += ord(list1[i])  # adds the chars together

    for i in range(len(plaintext)):  # goes through an array of plaintext
        char1 = plaintext[i]
        char1num = (ord(char1) + num - 11) % 116 + 11
        # turns the char into an int and
        # adds password to it then mods it so it is under 127 and above 11 in the ascii values
        ciphertext += chr(char1num)  # adds the new char to the cipher text
    return ciphertext


def caesarshiftde(key, ciphertext):
    """
    :return plaintext: clear text for caesar shift
    :param key: key: Takes in a string and counts every char to get a num for password
    :param ciphertext: takes in a string of chars to be decrypted
    """

    plaintext = ""
    num = 0
    list1 = list(key)
    for i in range(len(list1)):
        num = num + ord(list1[i])

    for i in range(len(ciphertext)):
            char1 = ord(ciphertext[i])
            check = True
            while check:
                if(char1 - num) < 11:  # if the value was modded then adds 126 to
                    # start the loop when below 11
                    char1 = char1 + 116
                else:
                    char1num = (char1 - num)
                    check = False
            plaintext += chr(char1num)
    return plaintext


def caesarshiftbrute(ciphertext):
    """
    :return results: and array of all the letters shifted 1 to 120 chars over
    :param ciphertext: takes in a string of chars to be decrypted
    """

    results = ""
    # starts a key at 1 and goes to 120 incrementing by 1
    for key in range(1, 120, 1):
        translated = ''
        for char in ciphertext:
            charnum = ord(char)  # gets the char from the cipher text
            charnum = charnum - key
            check1 = True
            while(check1):
                if charnum < 11:  # if the char was modded then restart the loop at 126, does not need chars under 30 for english
                    charnum += 116
                else:
                    check1 = False
            translated += chr(charnum)

        results += ('key #%s: %s\n======================\n' % (key, translated))
    return results


def monoalphabeticen(key, plaintext):
    """
    :return ciphertext: Encrypted text for monoalphabetic cipher
    :param key: Takes in a string for password to be used to encrypt the plaintext
    :param plaintext: takes in a string of chars to be encrypted
    """
    ciphertext = ""
    num = 0
    list1 = list(key)
    for i in range(len(list1)):  # counts the password
        num = num + ord(list1[i])
    dict1 = {' ':'i','!':'P','"':'/','#':'x','$':'_',
             '%':'2','&':'T',"'":'d','(':'"',')':'8',
             '*':'F','+':'l',',':'|','-':';','.':'S',
             '/':'m','1':'~','2':'*','3':'7','4':'L',
             '5':'[','6':'s','7':'(','8':'9','9':'B',
             ':':'j',';':'}','<':'&','=':'G','>':'a',
             '?':'z','@':'C','A':'f','B':'>','C':'.',
             'D':'\\','E':'M','F':'R','G':'u','H':'4',
             'I':'A','J':'k','K':'{','L':'-','M':'=',
             'N':'H','O':'6','P':'3','Q':')','R':'t',
             'S':'e','T':'p','U':'$','V':'#','W':"'",
             'X':' ','Y':'!','Z':'K','[':'E','\\':'D',
             ']':'1','^':'5','_':'%','`':'J','a':'I',
             'b':'`','c':'Z','d':'y','e':'<','f':',',
             'g':'+','h':':','i':'@','j':'?','k':'w',
             'l':'r','m':'q','n':'o','o':'W','p':'O',
             'q':'v','r':'Q','s':'V','t':'N','u':'^',
             'v':']','w':'n','x':'g','y':'b','z':'c',
             '{':'h','|':'Y','}':'U','~':'X'}

    revdict1 = {
            'i':' ','P':'!','/':'"','x':'#','_':'$',
            '2':'%','T':'&','d':"'",'"':'(','8':')',
            'F':'*','l':'+','|':',',';':'-','S':'.',
            'm':'/','~':'1','*':'2','7':'3','L':'4',
            '[':'5','s':'6','(':'7','9':'8','B':'9',
            'j':':','}':';','&':'<','G':'=','a':'>',
            'z':'?','C':'@','f':'A','>':'B','.':'C',
            '\\':'D','M':'E','R':'F','u':'G','4':'H',
            'A':'I','k':'J','{':'K','-':'L','=':'M',
            'H':'N','6':'O','3':'P',')':'Q','t':'R',
            'e':'S','p':'T','$':'U','#':'V',"'":'W',
            ' ':'X','!':'Y','K':'Z','E':'[','D':'\\',
            '1':']','5':'^','%':'_','J':'`','I':'a',
            '`':'b','Z':'c','y':'d','<':'e',',':'f',
            '+':'g',':':'h','@':'i','?':'j','w':'k',
            'r':'l','q':'m','o':'n','W':'o','O':'p',
            'v':'q','Q':'r','V':'s','N':'t','^':'u',
            ']':'v','n':'w','g':'x','b':'y','c':'z',
            'h':'{','Y':'|','U':'}','X':'~',}
    if num % 2 == 0:
        ciphertable = dict1
    else:
        ciphertable = revdict1
    letters = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
    for i in plaintext:
        if i in letters:
            ciphertext += ciphertable[i]
        else:
            ciphertext += i
    return ciphertext


def monoalphabeticde(key, ciphertext):
    """
    :return plaintext: decrypted text for monoalphabetic cipher
    :param key: Takes in a string for password to be used to encrypt the plaintext
    :param ciphertext: takes in a string of chars to be encrypted
    """
    plaintext = ""
    num = 0
    list1 = list(key)
    for i in range(len(list1)):  # counts the password
        num = num + ord(list1[i])

    dict1 = {' ':'i','!':'P','"':'/','#':'x','$':'_',
             '%':'2','&':'T',"'":'d','(':'"',')':'8',
             '*':'F','+':'l',',':'|','-':';','.':'S',
             '/':'m','1':'~','2':'*','3':'7','4':'L',
             '5':'[','6':'s','7':'(','8':'9','9':'B',
             ':':'j',';':'}','<':'&','=':'G','>':'a',
             '?':'z','@':'C','A':'f','B':'>','C':'.',
             'D':'\\','E':'M','F':'R','G':'u','H':'4',
             'I':'A','J':'k','K':'{','L':'-','M':'=',
             'N':'H','O':'6','P':'3','Q':')','R':'t',
             'S':'e','T':'p','U':'$','V':'#','W':"'",
             'X':' ','Y':'!','Z':'K','[':'E','\\':'D',
             ']':'1','^':'5','_':'%','`':'J','a':'I',
             'b':'`','c':'Z','d':'y','e':'<','f':',',
             'g':'+','h':':','i':'@','j':'?','k':'w',
             'l':'r','m':'q','n':'o','o':'W','p':'O',
             'q':'v','r':'Q','s':'V','t':'N','u':'^',
             'v':']','w':'n','x':'g','y':'b','z':'c',
             '{':'h','|':'Y','}':'U','~':'X'}

    revdict1 = {
            'i':' ','P':'!','/':'"','x':'#','_':'$',
            '2':'%','T':'&','d':"'",'"':'(','8':')',
            'F':'*','l':'+','|':',',';':'-','S':'.',
            'm':'/','~':'1','*':'2','7':'3','L':'4',
            '[':'5','s':'6','(':'7','9':'8','B':'9',
            'j':':','}':';','&':'<','G':'=','a':'>',
            'z':'?','C':'@','f':'A','>':'B','.':'C',
            '\\':'D','M':'E','R':'F','u':'G','4':'H',
            'A':'I','k':'J','{':'K','-':'L','=':'M',
            'H':'N','6':'O','3':'P',')':'Q','t':'R',
            'e':'S','p':'T','$':'U','#':'V',"'":'W',
            ' ':'X','!':'Y','K':'Z','E':'[','D':'\\',
            '1':']','5':'^','%':'_','J':'`','I':'a',
            '`':'b','Z':'c','y':'d','<':'e',',':'f',
            '+':'g',':':'h','@':'i','?':'j','w':'k',
            'r':'l','q':'m','o':'n','W':'o','O':'p',
            'v':'q','Q':'r','V':'s','N':'t','^':'u',
            ']':'v','n':'w','g':'x','b':'y','c':'z',
            'h':'{','Y':'|','U':'}','X':'~',}
    if num % 2 == 0:
        plaintable = revdict1
    else:
        plaintable = dict1
    letters = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
    for i in ciphertext:
        if i in letters:
            plaintext += plaintable[i]
        else:
            plaintext += i

    return plaintext

def polyalphabeticen(key, plaintext):
    """
    :return ciphertext: Encrypted text for  polyalphabetic cipher
    :param key: Takes in a string for password to be used to encrypt the plaintext
    :param plaintext: takes in a string of chars to be encrypted
    """
    ciphertext = ""

    num1 = 0
    list1 = list(key)
    for i in range(int(len(list1)/2)):  # counts first half of the password
        num1 = num1 + ord(list1[i])
    num2 = 0
    for i in range(int(len(list1)/2), len(list1), 1):  # counts second half of the password
        num2 = num2 + ord(list1[i])

    key1 = "1122121221"
    key2 = "2121221122"  # choose when to do the caesar ciphers
    if (num1 + num2)%2:
        mainkey = key1
    else:
        mainkey = key2

    for i in range(len(plaintext)):  # switch between the two caesar ciphers
        char1 = plaintext[i]

        if mainkey[i%10] == "1":
            char1num = (ord(char1) + num1 - 11) % 116 + 11
            ciphertext += chr(char1num)
        if mainkey[i%10] == "2":
            char1num = (ord(char1) + num2 - 11) % 116 + 11
            ciphertext += chr(char1num)

    return ciphertext

def polyalphabeticde(key, ciphertext):
    """
    :return plaintext: Encrypted text for  polyalphabetic cipher
    :param key: Takes in a string for password to be used to encrypt the plaintext
    :param ciphertext: takes in a string of chars to be encrypted
    """
    plaintext = ""

    num1 = 0
    list1 = list(key)
    for i in range(int(len(list1)/2)):  # counts first half of the password
        num1 = num1 + ord(list1[i])
    num2 = 0
    for i in range(int(len(list1)/2), len(list1), 1):  # counts second half of the password
        num2 = num2 + ord(list1[i])

    key1 = "1122121221"
    key2 = "2121221122"
    if (num1 + num2)%2:
        mainkey = key1
    else:
        mainkey = key2
    for i in range(len(ciphertext)):
            char1 = ord(ciphertext[i])
            check = True

            if mainkey[i%10] == "1":
                while check:
                    if(char1 - num1) < 11:  # if the value was modded then adds 126 to
                        # start the loop when below 11
                        char1 = char1 + 116
                    else:
                        char1num = (char1 - num1)
                        check = False
            if mainkey[i%10] == "2":
                while check:
                    if(char1 - num2) < 11:  # if the value was modded then adds 126 to
                        # start the loop when below 11
                        char1 = char1 + 116
                    else:
                        char1num = (char1 - num2)
                        check = False

            plaintext += chr(char1num)


    return plaintext


def blockcipheren(key, plaintext):
    """
    :return ciphertext: Encrypted text for block cipher
    :param key: Takes in a string for password to be used to encrypt the plaintext
    :param plaintext: takes in a string of chars to be encrypted
    """
    ciphertext = plaintext

    return ciphertext


def blockcipherde(key, plaintext):
    """
    :return ciphertext: Encrypted text for block cipher
    :param key: Takes in a string for password to be used to encrypt the plaintext
    :param plaintext: takes in a string of chars to be encrypted
    """
    ciphertext = plaintext

    return ciphertext


def streamcipheren(key, plaintext):
    """
    :return ciphertext: Encrypted text for stream cipher
    :param key: Takes in a string for password to be used to encrypt the plaintext
    :param plaintext: takes in a string of chars to be encrypted
    """
    ciphertext = plaintext

    return ciphertext


def streamcipherde(key, plaintext):
    """
    :return ciphertext: Encrypted text for stream cipher
    :param key: Takes in a string for password to be used to encrypt the plaintext
    :param plaintext: takes in a string of chars to be encrypted
    """
    ciphertext = plaintext

    return ciphertext


def cipherchoiceen(cipher5, input1, key):
        if cipher5 == 0:
            print("Poly Encrypt")
            key = "12345"
            return polyalphabeticen(key, input1)
        elif cipher5 == 1:
            print("Caesar Encrypt")
            return caesarshiften(key, input1)
        elif cipher5 == 2:
            print("Mono Encrypt")
            return monoalphabeticen(key, input1)
        elif cipher5 == 3:
            print("Poly Encrypt")
            return polyalphabeticen(key, input1)
        elif cipher5 == 4:
            print("Block Encrypt")
            return blockcipheren(key, input1)
        elif cipher5 == 5:
            print("Stream Encrypt")
            return streamcipheren(key, input1)

def cipherchoicede(cipher5, input1, key):
        if cipher5 == 0:
            print("Poly Decrypt")
            key = "12345"
            return polyalphabeticde(key, input1)
        elif cipher5 == 1:
            print("Caesar Decrypt")
            return caesarshiftde(key, input1)
        elif cipher5 == 2:
            print("Mono Decrypt")
            return monoalphabeticde(key, input1)
        elif cipher5 == 3:
            print("Poly Decrypt")
            return polyalphabeticde(key, input1)
        elif cipher5 == 4:
            print("Block Decrypt")
            return blockcipherde(key, input1)
        elif cipher5 == 5:
            print("Stream Decrypt")
            return streamcipherde(key, input1)

