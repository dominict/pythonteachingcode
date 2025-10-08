'''
To use this code, you will first need to install the three packages being imported below using pip or a manual install method.
This code was updated in August 2021 to use the new KSU news feed design.
'''
from bs4 import BeautifulSoup
import requests
import csv
from datetime import datetime

def scrape_ksu(ksu_url, page):
    '''
    This function is made for scraping the KSU news feed as of its redesign in August 2022.
    Now returns rows instead of writing a CSV.
    '''
    # grab the basic content from a web page
    source = requests.get(ksu_url + page).text
    # using the lxml parser to process the web page text content
    soup = BeautifulSoup(source, 'lxml')

    # find posts
    blog_list = soup.find('ul', class_='blog_listing')
    blog_posts = blog_list.find_all('li')

    rows = []
    i = 1
    for blog_post in blog_posts:
        title = blog_post.h3.text

        date = blog_post.p.text
        date = date.strip().strip('"').strip()

        URL = blog_post.find('a')['href']

        rows.append([i, title, URL, date])
        i += 1

    return rows

# -------- main driver: scrape many pages, write one CSV --------
all_rows = []
base_url = 'https://www.kennesaw.edu/news/news-releases/index.php?&p='

# loop the pages you want (1..9); adjust range as needed
for i in range(1, 10):
    page_rows = scrape_ksu(base_url, str(i))
    all_rows.extend(page_rows)

# write everything once into one CSV
outfile = f"ksu_news_{datetime.now():%m_%d_%Y}_all.csv"
with open(outfile, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Number", "Title", "URL", "Date"])
    writer.writerows(all_rows)

print(f"Wrote {len(all_rows)} rows to {outfile}")
