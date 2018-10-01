# Web Crawler: GitHub Remaster
from bs4 import BeautifulSoup
import requests
import sys

# Block URL keywords that make things boring
blacklist = {
    'facebook',
    'twitter',
    'github',
    'reddit',
    'google',
    'youtube',
    'amazon',
    'apple',
    'instagram',
    'tumblr',
    'tv',
    'redirect',
    'account',
    'register',
    'signin',
    'login',
    'policy',
    'legal',
    'terms',
    'shop',
    'store',
    'product',
}

# Recursive function to crawl hrefs
def crawl(url):

  # Append site being visited to list file
  visited = open('visited.txt', 'a')
  visited.write(url + ',')
  visited.close()

  # Get page from URL
  page = requests.get(url).text
  soup = BeautifulSoup(page, 'html.parser')

  # Loop through every anchor on page
  for link in soup.find_all('a'):

    # Get href if it exists
    href = link.get('href')
    if not href:
      continue

    # Avoid loops like foo.com/upload/upload/upload/upload/...
    if href.startswith('/'):
      continue
    # Avoid loops like foo.com////////////...
    if href.endswith('/'):
      href = href[:-1]

    # Checks that link does not contain blacklist keyword
    ok = False
    for item in blacklist:
      if item in href:
        break
    else:
      ok = True
    if not ok: continue

    # Checks that link is a thing on the internet
    try:
      requests.get(href)
    except:
      continue

    # Check that link has not already been visited
    ok = False
    visited = open('visited.txt', 'r')
    for visit in visited.read().split(','):
      if href == visit:
        break
    else:
      ok = True
    visited.close()
    if not ok: continue

    # Print and recursively crawl href if all conditions are met
    print(href)
    crawl(href)
 
# Start crawling on input URL:
try:
  initURL = sys.argv[1]
except IndexError:
  print('input site to visit as command line argument')
try:
  requests.get(initURL)
except:
  print('URL is invalid, try a different one')
crawl(initURL)
