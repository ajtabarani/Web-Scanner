#Abraham Tabarani
#November 8, 2022

#Web Scanner - Main

import SearchMethods
import TextScanner
import InfoStorage

def main():
    data=dict() #Data Storage

    #Method of Storage
    fileName=input('Enter desired file name: ')
    print()
    storageType=input('Select data storage method:\nText: T\nExcel: E\nSQL: S\nAnswer: ')
    print()

    while True:
        if(storageType.lower() in ('t','e','s')):
            break
        else:
            storageType=input('Invalid Answer. Please try again: ')
            print()

    #Search through URL or brower keyword
    methodInput=input('Select search type:\nBrowser: B\nURL: U\nAnswer: ')
    print()

    while True:
        if(methodInput.lower()=='u'): #URL Search
            searchType=input('Select desired data:\nKeywords: K\nEmails: E\nAnswer: ') #Search for keywords or email
            print()

            while True:
                if(searchType.lower()=='k'): #URL/Keyword Search
                    #Enter URL
                    url=input('Enter a URL: ')
                    print()

                    #Recursive?
                    recursiveInput=input('Open links into other pages (Y/N): ')
                    print()

                    recursive=False
                    while True:
                        if(recursiveInput.lower()=='y'):
                            recursive=True
                            break
                        elif(recursiveInput.lower()=='n'):
                            recursive=False
                            break
                        else:
                            recursiveInput=input('Invalid answer. Please try again: ')
                            print()
                    
                    #If recursive, depth?
                    if recursive:
                        maxLevel=input('Enter depth of search (exponential): ')
                        print()

                        while True:
                            if not maxLevel.isdigit():
                                maxLevel=input('Invalid answer. Enter an integer: ')
                                print()
                            else:
                                maxLevel=int(maxLevel)
                                break
                    else:
                        expand=False
                        maxLevel=0

                    #Enter Keywords
                    keyword1=input('Enter the first keyword: ')
                    keyword2=input('Enter the second keyword (Hit Enter to Move On): ')
                    keyword3=input('Enter the third keyword (Hit Enter to Move On): ')
                    print()

                    keywords = list(filter(None,[keyword1, keyword2, keyword3]))

                    try:
                        textDict=SearchMethods.urlSearch(url, recursive, 0, maxLevel)
                        data=TextScanner.phraseScan(textDict, keywords)
                        break
                    except:
                        print('URL not valid. Try again.\n')
                
                elif(searchType.lower()=='e'): #URL/Email Search
                    #Enter URL
                    url=input('Enter a URL: ')
                    print()

                    #Recursive?
                    recursiveInput=input('Open links into other pages (Y/N): ')
                    print()

                    recursive=False
                    while True:
                        if(recursiveInput.lower()=='y'):
                            recursive=True
                            break
                        elif(recursiveInput.lower()=='n'):
                            recursive=False
                            break
                        else:
                            recursiveInput=input('Invalid answer. Please try again: ')
                            print()
                    
                    #If recursive, depth?
                    if recursive:
                        maxLevel=input('Enter the depth of the search (exponential): ')
                        print()

                        while True:
                            if not maxLevel.isdigit():
                                maxLevel=input('Invalid answer. Enter an integer: ')
                                print()
                            else:
                                maxLevel=int(maxLevel)
                                break
                    else:
                        expand=False
                        maxLevel=0
                    try:
                        textDict=SearchMethods.urlSearch(url, recursive, 0, maxLevel)
                        data=TextScanner.emailScanDict(textDict)
                        break
                    except:
                        print('URL not valid. Try again.\n')
                
                else:
                    searchType=input('Invalid answer. Please try again: ')
                    print()
            break

        elif(methodInput.lower()=='b'): #Browser Search
            #Search for keywords or email
            searchType=input('Select desired data:\nKeywords: K\nEmails: E\nAnswer: ')
            print()

            while True:
                if(searchType.lower()=='k'): #Browser/Keyword Search
                    #Enter Search Keyword
                    searchKeyword=input('Enter Search Keyword: ')
                    print()

                    #Enter Number of Pages
                    pages=input('Enter number of pages to search: ')
                    print()

                    while True:
                        if not pages.isdigit():
                            pages=input('Invalid answer. Enter an integer: ')
                            print()
                        else:
                            pages=int(pages)
                            break
                    
                    #Enter Search Keywords
                    keyword1=input('Enter the first keyword: ')
                    keyword2=input('Enter the second keyword (Hit Enter to Move On): ')
                    keyword3=input('Enter the third keyword (Hit Enter to Move On): ')
                    print()

                    keywords = list(filter(None,[keyword1, keyword2, keyword3]))
                    
                    textDict=SearchMethods.browserSearch(searchKeyword, pages)
                    data=TextScanner.phraseScan(textDict, keywords)
                    break

                elif(searchType.lower()=='e'): #Browser/Email Search
                    #Enter Search Keyword
                    searchKeyword=input('Enter Search Keyword: ')
                    print()

                    #Enter Number of Pages
                    pages=input('Enter number of pages to search: ')
                    print()

                    while True:
                        if not pages.isdigit():
                            pages=input('Invalid answer. Enter an integer: ')
                        else:
                            pages=int(pages)
                            break

                    textDict=SearchMethods.browserSearch(searchKeyword, pages)
                    data=TextScanner.emailScanDict(textDict)
                    break

                else:
                    searchType=input('Invalid answer. Please try again: ')
                    print()
            break

        else:
            methodInput=input('Invalid answer. Please try again: ')
            print()
    
    #Storage
    if storageType=='t':
        InfoStorage.storeText(data, fileName)
    elif storageType=='e':
        InfoStorage.storeExcel(data, fileName)
    else:
        InfoStorage.storeSQL(data, fileName)

main()