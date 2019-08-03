'''
@Author: Galen Garofalo
Date: 7/24/19
Description: A list of encryption/decryption tools
'''
import random

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
            char1num = (ord(char1) + num1 - 10) % 116 + 10
            ciphertext += chr(char1num)
        if mainkey[i%10] == "2":
            char1num = (ord(char1) + num2 - 10) % 116 + 10
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


def vigenerecipheren(key, plaintext):
    ciphertext = ""
    charnum = []
    for i in key:
        charnum.append(ord(i))

    for i in range(len(plaintext)):  # switch between the two caesar ciphers
            char1 = plaintext[i]
            char1num = (ord(char1) + charnum[i % len(charnum)] - 11) % 116 + 11
            ciphertext += chr(char1num)

    return ciphertext


def vigenerecipherde(key, ciphertext):
    plaintext = ""
    charnum = []
    for i in key:
        charnum.append(ord(i))

    for i in range(len(ciphertext)):
            char1 = ord(ciphertext[i])
            check = True
            while check:
                if(char1 - charnum[i % len(charnum)]) < 11:  # if the value was modded then adds 126 to
                    # start the loop when below 11
                    char1 = char1 + 116
                else:
                    char1num = (char1 - charnum[i % len(charnum)])
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


def blockcipherde(key, ciphertext):
    """
    :return plaintext: Encrypted text for block cipher
    :param key: Takes in a string for password to be used to encrypt the plaintext
    :param ciphertext: takes in a string of chars to be decrypted
    """
    plaintext = ciphertext

    return plaintext


def streamcipheren(key, plaintext):
    """
    :return ciphertext: Encrypted text for stream cipher
    :param key: Takes in a string for password to be used to encrypt the plaintext
    :param plaintext: takes in a string of chars to be encrypted
    """
    ciphertext = plaintext

    return ciphertext


def streamcipherde(key, ciphertext):
    """
    :return plaintext: Encrypted text for stream cipher
    :param key: Takes in a string for password to be used to encrypt the plaintext
    :param ciphertext: takes in a string of chars to be decrypted
    """
    plaintext = ciphertext

    return plaintext


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
        elif cipher5 == 6:
            print("Vigenere Encrypt")
            return vigenerecipheren(key, input1)


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
        elif cipher5 == 6:
            print("Vigenere Decrypt")
            return vigenerecipherde(key, input1)

def RSAKeyGen(switch, p, q, timeout = -1):
    if(switch == 1):
        e = 3
        check5 = True
        # Given e = 3 find Public and Private
        while(check5):
            p, q =RSA_utils.findpq(e, p, q)
            z= (p-1)*(q-1)
            n= p*q
            print("Z: %s N: %s" % (str(z), str(n)))
            d= RSA_utils.findd(e, z, timeout)
            if(d == -1):
                print("D Timed out")
            else:
                check5 = False
            print("E: %s D: %s" % (str(e), str(d)))
            print("==============")
    elif(switch == 2):
        e = 65537
        # Given e = 65537 find Public and Private
        while(check5):
            p, q =RSA_utils.findpq(e, p, q)
            z= (p-1)*(q-1)
            n= p*q
            print("Z: %s N: %s" % (str(z), str(n)))
            d= RSA_utils.findd(e, z, timeout)
            if(d == -1):
                print("D Timed out")
            else:
                check5 = False
            print("E: %s D: %s" % (str(e), str(d)))
            print("==============")
    elif(switch == 3):
        # Given set of the largest primes p and q find Public and Private
        p= (pow(2, 82589933) -1)
        q= (pow(2, 77232917) -1)
        n = p*q
        z= (p-1)*(q-1)
        e= RSA_utils.finde(z)
        d= RSA_utils.findd(e, z, timeout)
        if(d == -1):
                print("D Timed out")
    elif(switch == 4):
        # Given set of the 160 digit primes p and q find Public and Private
        p= 5166566839092074458466334866571597694114460570387986357538048450432901440804868689337999823161841839689242893622491638917313351308387294478994745350551549126803
        q= 1081298104698286063813737967304568031406522676857739555339880517562925221530558524296599584286163751908713364829390795648074146197550782524900963175263757603219
        n = p*q
        z= (p-1)*(q-1)
        e= RSA_utils.finde(z)
        d= RSA_utils.findd(e, z, timeout)
        if(d == -1):
                print("D Timed out")
    elif(switch == 5):
        # Given set of 10 digit primes p and q find Public and Private
        p= 5915587277
        q= 1500450271
        n = p*q
        z= (p-1)*(q-1)
        e= RSA_utils.finde(z)
        d= RSA_utils.findd(e, z, timeout)
        if(d == -1):
                print("D Timed out")
    elif(switch == 6):
        n = 236303269
        e = 3
        d = 157514867
    else:
        # Given p and q find Public and Private
        n = p*q
        z= (p-1)*(q-1)
        e= RSA_utils.finde(z)
        d= RSA_utils.findd(e, z, timeout)
        if(d == -1):
                print("D Timed out")

    publickey = (n, e)
    privatekey = (n, d)
    return (publickey, privatekey)


def RSAen(pk, plaintext):
    n, e = pk
    ciphertext = [pow(ord(char), e, n) for char in plaintext]
    cipher = ''.join(map(lambda x: str(str(x)+ " "), ciphertext))
    return cipher


def RSAde(pk, ciphertext):
    n, d = pk
    cipher = ciphertext.split(" ")
    cipher.pop()
    print("Decrypting... This could take a while...")
    plaintext = [chr(pow(int(char), d, n)) for char in cipher]
    return ''.join(plaintext)


class RSA_utils:
    def findd(e, z, time= -1):
        if time == -1:
            timeout = False
        else:
            time = 100000000 * time
        check2 = True
        d = 0
        while(check2):
            d+=1
            if(d %100000000 == 0):
                print(str(d))
            if((e*d) % z == 1):
                check2 = False
            if(d %time== 0 and timeout):
                d = -1
                break
        return d


    def finde(z):
        check =True
        e = 1
        while(check):
            count = 0
            e += 1
            print("test e: " +str(e))
            for i in range(1, min(e, z)+1):
                if e % i == z % i == 0:
                    count += 1
                    print("--Count: "+str(count))
            if(count <= 1 or e>z):
                check = False
        return e

    def findpq(e, min, max):
        p = 0
        q = 0
        random.seed()
        check1 = True
        e = e*2
        lowprime= [3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97
                   ,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179
                   ,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269
                   ,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367
                   ,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461
                   ,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571
                   ,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661
                   ,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773
                   ,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883
                   ,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997]
        while(check1):
            prime =random.randint(min, max)
            for i in lowprime:
                if(prime % i == 0):
                    if(prime != i):
                        break
            a = random.randint(0, prime)
            test = pow(a, prime-1)% prime
            if(test == 1):
                p = prime
                check1 = False
        check1 = True
        while(check1):
            prime = random.randint(min, max)
            for i in lowprime:
                if(prime % i == 0):
                    break
            a = random.randint(0, prime)
            test = pow(a, prime-1)% prime
            if(test == 1 and p != prime):
                q = prime
                check1 = False
        if(p > q):
            temp = p
            p = q
            q = temp
        print("P: "+str(p) + " Q: " +str(q))
        return (p, q)


if __name__ == '__main__':
    # Test encrypt cases
    # publickey, privatekey = RSAKeyGen(1, 1000, 9000)
    #publickey = (236303269, 3)
    #privatekey = (236303269, 157514867)
    publickey, privatekey = RSAKeyGen(1, 100000, 1000000, -1)
    print("==============")
    print("Public: "+str(publickey))
    print("Private: "+str(privatekey))
    print("==============")
    input1 = "Hello, How are you today?"
    print("Input: " + input1)
    out = RSAen(publickey, input1)
    print("En: " + out)
    out = RSAde(privatekey, out)
    print("De: " + out)
