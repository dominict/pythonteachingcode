'''
This code goes out to the Web and gets a web page and parses it into local data.
To use this code, you will first need to install the three packages being imported below using pip.
'''
from bs4 import BeautifulSoup
import requests
import csv
source = requests.get('http://coreyms.com').text
soup = BeautifulSoup(source, 'lxml')
#print(soup.prettify())
#article = soup.find('article')
#method to get all
articles = soup.find_all('article')
#print(article.prettify())
for article in articles:
    headline = article.h2.a.text
    print(headline)
    summary = article.find('div', class_='entry-content').p.text
    print(summary)
    #This try/except block handles the situation when a video is
    try:
        vid_src = article.find('iframe', class_='youtube-player')['src']
        #print(vid_src)
        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]
        #print(vid_id)
        #f method below is only avilable in Python 3.6 and after
        yt_link = f'https://youtube.com/watch?v={vid_id}'
    except Exception as e:
        yt_link = None
    print(yt_link)
    print()
