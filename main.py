import re
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
 
text=regex.sub('',input("    ").lower())
crib=input("    ").lower()
plaintexts=decrypt(text)
while True:
    for el in plaintexts:
        if crib in el:
            input(el)
