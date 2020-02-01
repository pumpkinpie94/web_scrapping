## script to download news articles from page html, created by pumpkinpie94 on 1/25/2020
from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.nytimes.com/2018/11/11/business/intelligence-expert-wall-street.html').text

soup = BeautifulSoup(source, 'lxml')

for text in soup.find_all('p'):
    print(text.text)
    print()

#print(soup.prettify())