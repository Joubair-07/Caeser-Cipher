"""Caeser cipher, By Joubair alphajoubair@gmail.com
This program encrypt/decrypt text messages using caeser cipher by
Julius Caeser."""

import caeser_functions as cf
import pyperclip as pc    # to copy text to clipboard


# All symbols that will be encrypted.
# Evert possible symbol:
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '

maxkey = len(SYMBOLS) - 1  

def main():

    cf.intro()
    mode = cf.getMode()
    key = cf.getKey(maxkey) 
    message = cf.getMssg(mode).upper()

    # Show resultes for (e/d) message.
    if mode == 'encrypt':
        encryptedMessage = cf.encrypt(message, SYMBOLS, key)
        print(encryptedMessage)
        pc.copy(encryptedMessage)
        print('Full encrypted text copied to clipboard!')


    elif mode == 'decrypt':
        decryptedMessage =  cf.decrypt(message, SYMBOLS, key)
        print(decryptedMessage)




if __name__ == '__main__':
    main()
