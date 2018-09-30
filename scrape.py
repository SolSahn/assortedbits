# Very, very sloppy web scraper, but it works
from bs4 import BeautifulSoup
import requests

visited = []
def scrapeLinks(url):
  global visited
  visited.append(url)
  page = requests.get(url).text
  soup = BeautifulSoup(page, 'html.parser')
  for link in soup.find_all('a'):
    visitLink = True
    href = link.get('href')
    try:
      if href[0] == '/':
        visitLink = False
      if href.endswith('/'):
        href = href[:-1]
      for visit in visited:
        if href == visit:
          visitLink = False
          break
    except:
      visitLink = False
    try:
      requests.get(href)
    except:
      visitLink = False
    if visitLink:
      print(href)
      scrapeLinks(href)

# Put url to start with in here:
scrapeLinks('https://xkcd.com')
