#Abraham Tabarani
#November 8, 2022

#Web Scanner - SearchMethods

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def urlSearch(url, recursive, currentLevel, maxLevel):
    #Selenium Setup and URL Opening
    PATH='C:\Program Files (x86)\chromedriver.exe'
    chromeOptions = Options()
    chromeOptions.add_argument("--headless")
    chromeOptions.add_argument("--width=1920")
    chromeOptions.add_argument("--height=1080")
    driver=webdriver.Chrome(chrome_options=chromeOptions, executable_path=PATH)
    driver.get(url)

    #Pulls source code and parses
    page_source=driver.page_source #Pulls all code
    soup=BeautifulSoup(page_source, 'html.parser') #Parses code
    
    #Pulls text and adds to return set
    returnDict=dict()
    tempString=''
    for temp in soup.findAll(text=True):
        tempString+=temp
    returnDict[url]=tempString

    if recursive: #Checks recursive
        if int(currentLevel) < int(maxLevel): #Checks if exceeding maxLevel
            currentLevel+=1

            links=set()
            aTags=set(soup.findAll('a')) #Set Removes Duplicates
            for aTag in aTags:
                links.add(aTag.get('href'))

            for link in links: #Finds all link tags
                if link[0:8]=='https://':
                    try:
                        returnDict=returnDict | urlSearch(link, recursive, currentLevel, maxLevel)
                    except:
                        print("Exception occured.")
                elif link[0]=='/':
                    baseLink = urlparse(url).netloc
                    link="https://"+baseLink+link
                    try:
                        returnDict=returnDict | urlSearch(link, recursive, currentLevel, maxLevel)
                    except:
                        print("Exception occured.")

    return returnDict

def browserSearch(keyword, searchNumber):
    #Selenium Setup and URL Opening
    PATH='C:\Program Files (x86)\chromedriver.exe'
    chromeOptions = Options()
    chromeOptions.add_argument("--headless")
    chromeOptions.add_argument("--width=1920")
    chromeOptions.add_argument("--height=1080")
    driver=webdriver.Chrome(chrome_options=chromeOptions, executable_path=PATH)
    driver.get('https://www.google.com/search?q=' + keyword)

    #Pulls source code and parses
    page_source=driver.page_source #Pulls all code
    soup=BeautifulSoup(page_source, 'html.parser') #Parses code

    #Initialize Return List
    returnDict=dict()

    divTags=soup.findAll('div', class_ = 'yuRUbf')
    for divTag in divTags[0:searchNumber]:
        split = str(divTag).split(' ')
        link = split[5][6:-10] #Extracts link from div tag

        driver2=webdriver.Chrome(chrome_options=chromeOptions, executable_path=PATH)
        driver2.get(link) #Enters the link

        page_source2=driver2.page_source #Pulls all code
        soup2=BeautifulSoup(page_source2, 'html.parser') #Parses code

        tempString=''
        for temp in soup2.findAll(text=True):
            tempString+=temp
        returnDict[link]=tempString

    return returnDict