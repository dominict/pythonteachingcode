'''
TO use this code, you will first need to install the three packages being imported below using pip or a manual install method.
'''
from bs4 import BeautifulSoup
import requests
import csv
from datetime import datetime

#grab the basic content from a web page
source = requests.get('https://www.kennesaw.edu/news/news-releases/index.php?&p=1').text
#using the lxml parser to process the web page text content
soup = BeautifulSoup(source, 'lxml')
#create a csv file in "w" write mode so we can add content to it. 
ksu_news_csv = open("ksu_news "+"{:%B %d, %Y}".format(datetime.now())+".csv","w")
csv_writer = csv.writer(ksu_news_csv)
#write the header row into our csv file
csv_writer.writerow(["Number","Title","URL","Date"])
#show the content of the website we retrieved so that we can find the unique tags around the content we want
#print(soup.prettify())

#blog_post = soup.find('ul',class_='two_col has_gap is_30')
#blog_post = soup.find('div',{"id":"main"})
blog_list = soup.find('ul',class_='blog_listing')
#print(blog_list.prettify())
blog_posts = blog_list.find_all('li')

#print(type(blog_posts))
#blog_posts = blog_posts.split("<li>")

i = 1
for blog_post in blog_posts:
    
    #print(i)
    title = blog_post.h3.text
    #print(title)
 
    date = blog_post.p.text
    date = date.strip()
    date = date.strip('"')
    date = date.strip()
    #print(date)
    
    
    URL = blog_post.find('a')['href']
    #print(URL)

    
    csv_writer.writerow([i,title,URL,date])

    i += 1
    

ksu_news_csv.close()
