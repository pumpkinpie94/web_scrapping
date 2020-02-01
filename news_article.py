## script to download news articles from page html, created by pumpkinpie94 on 2/1/2020
from bs4 import BeautifulSoup
import requests
import re
import datetime
import os
from pathlib import Path

#path and document extension
home = str(Path.home())
userFolder = home + '/Documents'
finalFolder = userFolder + '/News_Articles/'
fileType = '.txt'

with os.scandir(userFolder) as drive:
    folder_exists = 0
    for folder in drive:
        if(folder.name == 'News_Articles'):
            folder_exists = 1
            break
    if(folder_exists != 1):
        os.mkdir(userFolder+'/News_Articles')


#get url from user
url = input("url of article:")

#supply url to requests to get html
source = requests.get(url).text

#give html to beautifulsoup to parse
soup = BeautifulSoup(source, 'lxml')

# attempt to get article title
realTitle = soup.find('h1')

#initiate filename for opening at end
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
    file = open(finalFolder+finalTitle+fileType, 'w')
    file.write(title)
    file.write('\n\n\n')

    #file name for os to open the txt document at the end
    fileName = finalFolder+finalTitle+fileType

else:
    #name and path of document
    print("Sorry, I was not able to find the title of the article. Please supply one.")
    title = input("Title:")

    #create document in specified path
    file = open(finalFolder+title+fileType, 'w')

    #file name for os to open the txt document at the end
    fileName = finalFolder+title+fileType

#write the article to the text file
for text in soup.find_all('p'):
    file.write(text.text)
    file.write("\n\n")

#put retrieved date and url at bottom of article
d = datetime.datetime.today()
file.write("retrieved on: " + d.strftime('%m-%d-%Y') + "\nretrieved from: " + url)

file.close
response = input("The Article is ready to be Read. It has been saved to your News_Articles folder. Enter \"Y\" to open now or \"N\" to read later.")
if(response == 'Y' or response == 'y'):
    os.startfile(fileName)