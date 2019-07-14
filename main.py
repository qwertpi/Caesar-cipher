#need regex for input sanititastion
import re
#need random numbers to perform random shifts
from random import randint

#regex that matches characters that are not lower case a-z and not upper case A-Z
regex = re.compile('[^a-zA-Z]')

#takes a list and returns a list sorted by the number of times the elements occured in the original list
def SortList(l):
    '''
    Removes duplicates and sorts a list by how many duplicates there were
    :param l: list, the list to be sorted
    :return: a list in decending order of the number of duplicates
    '''
    #creates a dictionary with the keys of the list elements and values of how often the key appears in the list
    l = { x: l.count(x) for x in set(l) }
    #sorts the dict by the keys and pulls out the keys
    l = [x for x in sorted(l, key=l.get, reverse=True)]
    return l
    
def NgramFinder(text, n=2):
    '''
    Finds ngrams in a string
    :param text: string, the string to search for ngrams input
    :param n: int, the n value for the n gram eg. 2 for bigram, 3 for trigram etc.
    :return: a list of all the ngrams (may contain duplicates)
    '''
    grams = []
    i = 0
    try:
        while True:
            ngram = text[i]
            #bigram needs current character and one character ahead, trigram needs up to second character etc.
            for step in range(1,n):
                ngram+=text[i+step]
            grams.append(ngram)
            i+=1
    #once we get to the end of the string an index error will be caused
    except IndexError:
        pass

    return grams

def encrypt(string,shift):
    '''
    Encrypts a string with the caeser cipher
    :param string: string, the string to encrypt
    :param shift: int, the shift to use
    :return: string, the encrypted text
    '''
    #inits the variable storing our ciphertext so that we can append to it
    ciphertext=""
    
    #loops over every character in the string
    #makes everything lowercase to make my life easier
    for char in string.lower():
        #if the character is alphabetical encrypts it
        if re.match("[a-z]", char):
            #gets the character as a ascii number 
            #subtracts 96 to make it a number from 1-26 
            #adds the shift
            #does modulo 26 so we wrap back around if we go above 26
            #adds 96 to turn it back into a valid asci character code
            #converts that number to a charcater 
            #and appends it to the ciphertext variable
            ciphertext+=chr(((ord(char)-96+shift)%26+96))

            #26=z but 26%26=0 which results in the ` character this fixes this
            #if the last character (the one we jsut appended) is an `
            if ciphertext[-1]=="`":
                #removes the last character
                ciphertext=ciphertext[:-1]
                #appends a z to cipher text
                ciphertext+="z"
        else:
            #adds non alphabetical characters as they are
            ciphertext += char
            
    return ciphertext

def decrypt(string,shift):
    '''
    Encrypts a string with the caeser cipher
    :param string: string, the string to encrypt
    :param shift: int, the shift to use
    :return: string, the encrypted text
    '''
    #decryption is just encrytion with a negative shift
    plaintext = encrypt(string, -shift)

    return plaintext

mode=input("Would you like to 1) Encrypt or 2) Decrypt    ").lower()

if mode=="1" or mode=="encrypt":
    text = input("Enter the text you wish to encrypt    ").lower()

    try:
        shift=int(input("Enter the shift you wish to use or leave blank to use a random shift    "))
        
    #if they left it blank the cast to int will fail raising this error
    except ValueError:
        shift=randint(1,26)

    print(encrypt(text,shift))
    print(shift)
    
elif mode=="2" or mode=="decrypt":
    text = input("Enter the text you wish to decrypt    ").lower()

    #opens the file if no text input was provided
    if text=="":
        try:
            with open("file.txt","r") as f:
                text = f.read().lower()
        except FileNotFoundError:
            print("No text was provided and the file file.txt doesn't exist, non-existant text can't be encrypted!")
    
    try:
        shift=int(input("Enter the shift if you know it else leave this blank    "))
        plaintext=decrypt(text,shift)
        print(plaintext)

    #if they left the shift blank the cast to int will fail raising this error
    except ValueError:
        crib=input("Enter a crib to search for in the posible decryptions if you know it else leave this blank    ").lower()

        plaintexts = [decrypt(text, shift) for shift in range(1,26)]
        #if they typed a crib
        if crib != "":
            #shows each of the plaintexts along with their shift
            while True:
                for el in plaintexts:
                    if crib in el:
                        print(abs(ord(el[1])-ord(text[1])))
                        input(el)
        else:
            #without a crib we fall back to bigrams and trigrams
            for el in plaintexts:
                #gets the bigrams and trigrams in the text in lists of decending order of frequency
                bigrams = SortList(NgramFinder(el))
                trigrams = SortList(NgramFinder(el, 3))
                #checks if any of the top three bigrams for enlish text are in the top two bigrams for this plaintext 
                #then does the same for trigrams
                if bigrams[0]=="th" or bigrams[1]=="th" or bigrams[0]=="he" or bigrams[1]=="he" or bigrams[0]=="in" or bigrams[1]=="in" or trigrams[0]=="the" or trigrams[1]=="the" or trigrams[0]=="and" or trigrams[1]=="and" or trigrams[0]=="ing" or trigrams[1]=="ing":
                    
                    print(abs(ord(el[0])-ord(text[0])))
                    input(el)
else:
    print("That mode doesn't exist, please restart the program")
