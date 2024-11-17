"""This model contain function to use in the main program (ceaserCipher.py)"""

def encrypt(message, symbols, key):
    """Encrypt each symbol in the message."""
    encryptedMssg = ''
    for symbol in message: # Take each letter from the message to encrypt it .
        num = symbols.find(symbol) # Get the the position of letter on symbols.
        num = num + key  # Add the key to number
        num = checkNum(num, symbols) # Check if number larger than len(symbols) or less than 0.
        if symbol in symbols: 
            encryptedMssg += symbols[num]
        elif symbol not in symbols:
            encryptedMssg += symbol # Add the letter withoud encrypt it .

    return encryptedMssg


def decrypt(message, symbols, key):
    """Decrypt each symbol in the message."""
    decryptedMssg = ''
    for symbol in message:
        num = symbols.find(symbol)
        num = num - key     # Substract the key from the number
        num = checkNum(num, symbols)
        if symbol in symbols:
            decryptedMssg += symbols[num]
        elif symbol not in symbols:
            decryptedMssg += symbol 

    return decryptedMssg



def checkNum(number, symbols):
    """Handle the wrap-around if num is larger then the lenght of SYMBOLS
    or less than 0."""
    if number >= len(symbols):
        number = number - len(symbols)
        return number

    elif number < 0:
        number = number + len(symbols)
        return number
    
    return number


def getMode():
    while True: # Keep asking the user until he enter a (e or d)
        mode = ''
        print('Do you want to (e)ncrypt or (d)ecrypt?')
        response = input('> ')
        if response.lower().startswith('e'):
            mode = 'encrypt'
            break
        elif response.lower().startswith('d'):
            mode = 'decrypt'
            break

    return mode


def getKey(maxkey):
    while True: # Keep asking the user until he enter a valid key.
        print('Please enter the key (0 to {}) to use.'.format(maxkey))
        response = input('> ')
        if not response.isdecimal():
            continue
        elif 0 <= int(response) <= maxkey:
            key = int(response)
            break
    
    return key


def getMssg(mode):
    """Print and return the message based on mode (e or d)"""
    print('Enter the message to {}'.format(mode))
    message = input('> ')
    return message


def intro():
    '''Printing an introduction for the program.'''

    print('''Caeser cipher, By Joubair alphajoubair@gmail.com
    The Caeser cipher encrypt letters by shifting them over by a
    key number. for exemple a key of 7 means the letter A is
    encrypted to H, the letter H is encrypted to I.''')
    print()

