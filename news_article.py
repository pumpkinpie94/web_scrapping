## script to download news articles from page html, created by pumpkinpie94 on 1/25/2020
from bs4 import BeautifulSoup
import requests
import re
import datetime
import os

#path and document extension
path = "B:/articles/"
fileType = '.txt'

#get url from user
url = input("url of article:")

#supply url to requests to get html
source = requests.get(url).text

#give html to beautifulsoup to parse
soup = BeautifulSoup(source, 'lxml')

# attempt to get article title
realTitle = soup.find('h1')

fileName = ''

#if title found use as document name and add to top of document
if(realTitle != None):
    #name and path of document
    title = realTitle.text
    #remove special characters from title
    docTitle = re.sub(r'\W+', ' ', title)
    #replace spaces with underscores
    finalTitle = docTitle.replace(' ', '_')
    print('Saved As: ',finalTitle+fileType)

    #create document in specified path
    file = open(path+finalTitle+fileType, 'w')
    file.write(title)
    file.write('\n\n\n')

    fileName = path+finalTitle+fileType

else:
    #name and path of document
    print("Sorry, I was not able to find the title of the article. Please supply one.")
    title = input("Title:")

    #create document in specified path
    file = open(path+title+fileType, 'w')

    fileName = path+title+fileType

#write the article to the text file
for text in soup.find_all('p'):
    file.write(text.text)
    file.write("\n\n")

#put retrieved date and url at bottom of article
d = datetime.datetime.today()
file.write("retrieved on: " + d.strftime('%m-%d-%Y') + "\nretrieved from: " + url)

file.close
input("The Article is read to be Read. Press enter to open and read it.")
os.startfile(fileName)