#need regex for input sanititastion
import re
#need random numbers to perform random shifts
from random import randint

#regex that matches characters that are not lower case a-z and not upper case A-Z
regex = re.compile('[^a-zA-Z]')

#takes a list and returns a list sorted by the number of times the elements occured in the original list
def SortList(l):
    #creates a dictionary with the keys of the list elements and values of how often the key appears in the list
    l = { x: l.count(x) for x in set(l) }
    #sorts the dict by the keys and pulls out the keys
    l = [x for x in sorted(l, key=l.get, reverse=True)]
    return l
def BigramFinder(text, n=2):
    grams = []
    i = 0
    step = n-1
    text_length = len(text)

    while i+step < text_length:
        ngram = text[i]
        for step in range(1,n):
            ngram+=text[i+step]
        grams.append(ngram)
        i+=1

    return grams

def encrypt(string,shift):
    #inits the variable storing our ciphertext so that we can append to it
    ciphertext=""
    
    #loops over every character in the string
    #makes everything lowercase to make my life easier
    for char in string.lower():
        #gets the character as a ascii number subtracts 96 to make it a number from 1-26 adds the shift that was passed as an argumet, does modulo 26 so we wrap back around if we go above 26, adds 96 to turn it back into a vlaid acci character code , converts that number to a charcater and appends it to the ciphertext variable
        ciphertext+=chr(((ord(char)-96+shift)%26+96))
        #26=z but 26%26=0 which results in the ` character this fixes this
        #if the last character (the one we jsut appended) is an `
        if ciphertext[-1]=="`":
            #removes the last character
            ciphertext=ciphertext[:-1]
            #appends a z to cipher text
            ciphertext+="z"
            
    return ciphertext

def decrypt(string,shift=""):
    #if we don't know the shift
    if shift=="":
        #inits the variable storing our plaintext so that we can append to it
        plaintext=""
        #inits the variable storing our possible plaintexts so that we can append to it
        plaintexts=[]
        #tries every shift from 1-26
        for shift in range (1,27):
            for char in string.lower():
                #same as the ciphertext code but - shift to reverse the shift
                plaintext+=chr(((ord(char)-96-shift)%26+96))
                #26=z but 26%26=0 which results in the ` character this fixes this
                if plaintext[-1]=="`":
                    plaintext=plaintext[:-1]
                    plaintext+="z"
            #appends this plaintext to the 
            plaintexts.append(plaintext)
            plaintext=""
        return plaintexts
    else:
        #inits the variable storing our plaintext so that we can append to it
        plaintext=""
        for char in string.lower():
            #same as the ciphertext code
            plaintext+=chr(((ord(char)-96-shift)%26+96))
            #26=z but 26%26=0 which results in the ` character this fixes this
            if plaintext[-1]=="`":
                plaintext=plaintext[:-1]
                plaintext+="z"
        return plaintext

mode=input("Would you like to 1) Encrypt or 2) Decrypt    ").lower()
if mode=="2" or mode=="decrypt":
    text=regex.sub('',input("Enter the text you wish to decrypt    ").lower())
    if text=="":
        try:
            with open("file.txt","r") as f:
                text=regex.sub('',f.read()).lower()
        except FileNotFoundError:
            pass
    try:
        shift=int(input("Enter the shift if you know it else leave this blank    "))
        plaintext=decrypt(text,shift)
        print(plaintext)
    except ValueError:
        crib=input("Enter a crib to search for in the posible decryptions if you know it else leave this blank    ").lower()

        plaintexts=decrypt(text)
        if crib != "":
            while True:
                for el in plaintexts:
                    if crib in el:
                        print(abs(ord(el[1])-ord(text[1])))
                        input(el)
        else:
            for el in plaintexts:
                bigrams = SortList(BigramFinder(el))
                trigrams = SortList(BigramFinder(el, 3))
                #checks if any of the top three bigrams for enlish text are in the top two bigrams for this plaintext then does the same for the trigrams
                if bigrams[0]=="th" or bigrams[1]=="th" or bigrams[0]=="he" or bigrams[1]=="he" or bigrams[0]=="in" or bigrams[1]=="in" or trigrams[0]=="the" or trigrams[1]=="the" or trigrams[0]=="and" or trigrams[1]=="and" or trigrams[0]=="ing" or trigrams[1]=="ing":
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
