## script to download news articles from page html, created by pumpkinpie94 on 1/25/2020
from bs4 import BeautifulSoup
import requests

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
realTitle = soup.find('span', class_='ghost')

#if title found use as document name and add to top of document
if(realTitle != None):
    #name and path of document
    title = realTitle.text

    #create document in specified path
    file = open(path+title+fileType, 'w')
    file.write(realTitle.text)
    file.write('\n\n\n')

else:
    #name and path of document
    print("Sorry, I was not able to find the title of the article. Please supply one.")
    title = input("Title:")

    #create document in specified path
    file = open(path+title+fileType, 'w')




for text in soup.find_all('p'):
    file.write(text.text)
    file.write("\n\n")

file.close
print("done writing file")
#print(soup.prettify())