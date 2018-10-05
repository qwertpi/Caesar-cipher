import re
from random import randint
regex = re.compile('[^a-zA-Z]')

def encrypt(string,shift):
    ciphertext=""
    for char in string.lower():
        ciphertext+=chr(((ord(char)-96+shift)%26+96))
    return ciphertext

def decrypt(string):
    plaintext=""
    plaintexts=[]
    for shift in range (1,27):
        for char in string.lower():
            plaintext+=chr(((ord(char)-96+shift)%26+96))
        plaintexts.append(plaintext)
        plaintext=""
    return plaintexts
mode=input("Would you like to 1) Encrypt or 2) Decrypt    ").lower()
if mode=="2" or mode=="decrypt":
    text=regex.sub('',input("Enter the text you wish to decrypt    ").lower())
    crib=input("Enter a crib to search for in the posible decryptions    ").lower()
    plaintexts=decrypt(text)
    while True:
        for el in plaintexts:
            if crib in el:
                print(abs(ord(el[1])-ord(text[1])))
                input(el)
elif mode=="1" or mode=="encrypt":
    text=regex.sub('',input("Enter the text you wish to encrypt    ").lower())
    try:
        shift=int(input("Enter the shift you wish to use or leave blank to use a random shift    "))
    except ValueError:
        shift=randint(1,26)
    print(encrypt(text,shift))
    print(shift)
