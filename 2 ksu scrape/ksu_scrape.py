'''
TO use this code, you will first need to install the three packages being imported below using pip or a manual install method.
'''
from bs4 import BeautifulSoup
import requests
import csv
from datetime import datetime


source = requests.get('http://news.kennesaw.edu/in-the-news/?&categories=in%20the%20news&year=2018').text

soup = BeautifulSoup(source, 'lxml')

ksu_news_csv = open("ksu_news "+"{:%B %d, %Y}".format(datetime.now())+".csv","w")
csv_writer = csv.writer(ksu_news_csv)

csv_writer.writerow(["Number","Title","Source","URL","Date"])

#print(soup.prettify())

#blog_post = soup.find('ul',class_='blog_listing')
blog_posts = soup.find('ul',class_='blog_listing')

blog_posts = blog_posts.find_all('li')

#print(type(blog_posts))
#blog_posts = blog_posts.split("<li>")
#print(blog_posts.prettify())

i = 1
for blog_post in blog_posts:
    
    #print(i)
    title = blog_post.a.text
    title = title.split("(")
    justtitle = title[0]
    #print(title[0])
    if len(title)>1:
        source = title[1].strip(")")
        #print(source)
    else:
        source = "No Source"
        #print(source)

    URL = blog_post.find('a')['href']
    #print(URL)

    date = blog_post.find("span").text
    date = date.strip()
    date = date.strip("–")
    date = date.strip()
    #print(date)
    csv_writer.writerow([i,justtitle,source,URL,date])

    i += 1
    print()

ksu_news_csv.close()