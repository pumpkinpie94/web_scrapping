from bs4 import BeautifulSoup
import requests
import re
import datetime
import os
from pathlib import Path
#test how it works
#with open('test.html') as html_file:
    #soup = BeautifulSoup(html_file, 'lxml')

#match = soup.title.text
#print(match)

#found = soup.find('div', class_='footer')
#print(found)

#for article in soup.find_all('div', class_='article'):
    #headline = article.h2.a.text
    #print(headline)

    #summary = article.p.text
    #print(summary)

    #print()

#print out what you found    
#print("here comes the code!!.....")
#print(soup.prettify())
#print("thanks god that's done! :)")

#test with live site and real article

#source = requests.get('https://www.nytimes.com/2018/11/11/business/intelligence-expert-wall-street.html').text

#soup = BeautifulSoup(source, 'lxml')

#for text in soup.find_all('p'):
#    print(text.text)
#    print()

#print(soup.prettify())

#find documents folder



#entries = os.scandir('C:')
#print(entries.name)

home = str(Path.home())
userFolder = home + '/Documents'

with os.scandir(userFolder) as drive:
    folder_exists = 0
    for folder in drive:
        print(folder.name)
        if(folder.name == 'news_articles'):
            print('folder found')
            folder_exists = 1
            break
    if(folder_exists != 1):
        os.mkdir(userFolder+'/news_articles')
        print('created folder')



