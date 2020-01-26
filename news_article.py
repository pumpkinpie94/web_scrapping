## script to download news articles from page html, created by pumpkinpie94 on 1/25/2020
import urllib.request
import urllib.error
import urllib.parse

url = 'https://www.theatlantic.com/ideas/archive/2020/01/american-housing-has-gone-insane/605005/?utm_source=pocket-newtab'
title = 'american housing has gone insane'
path = 'B:/articles/'
fileType = '.txt'
file = open(path+title+fileType, 'w')


response = urllib.request.urlopen(url)
webContent = response.read()
file.write(webContent.decode('utf-8'))
file.close()
print(webContent)