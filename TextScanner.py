#Abraham Tabarani
#November 8, 2022

#Web Scanner - TextScanner

import re

#Takes a string (may be a single word or entire page) and detects all emails within that page

initialEmailRegex=r'\b[\w.%+-]{1,}@[A-Za-z0-9-]{1,}\.[A-Z|a-z]{2,}\b'

def emailScanDict(dictionary):
    for key, value in dictionary.items():
        value=value.replace('\n', ' ')
        words=value.split(' ') #Splits string into words by space

        tempEmailSet=set()
        for word in words:
            word = word.strip('" ') #Strips all unwanted characters
            if(re.fullmatch(initialEmailRegex, word)): #Intial Filter
                username=word.split('@')[0]
                domainName=word.split('@')[1].split('.')[0]
                if not ('..' in username or username[0]=='.' or username[-1]=='.' or domainName[0]=='-' or domainName[-1]=='-'):
                    tempEmailSet.add(word)
        
        dictionary[key]=[*tempEmailSet, ]

    return dictionary

def emailScanString(string):
    returnSet={}
    words=string.split(' ') #Splits string into words by space

    for word in words:
        word=word.strip('" ') #Strips all unwanted characters
        if(re.fullmatch(initialEmailRegex, word)): #Intial Filter
            username=word.split('@')[0]
            domainName=word.split('@')[1].split('.')[0]
            if not ('..' in username or username[0]=='.' or username[-1]=='.' or domainName[0]=='-' or domainName[-1]=='-'):
                returnSet.add(word)
    
    return [*returnSet, ]

def phraseScan(dictionary, keywords):
    for key,value in dictionary.items(): #Iterates through dictionary(String, String) where latter is page text
        phrases=value.split('\n') #Splits text by newline
        tempInfoSet=set()
        for phrase in phrases:
            keepRunning=True
            words=phrase.split(' ')
            for word in words:
                 if len(word)>50: #Filters out gibberish code
                    keepRunning=False
                    break
            if keepRunning:
                for keyword in keywords:
                    if keyword in phrase and keepRunning:
                        tempInfoSet.add(phrase.strip()) #Adds stripped info to infoSet
                        break
        
        dictionary[key]=[*tempInfoSet, ] #Changes each key's value to formatted list

    return dictionary