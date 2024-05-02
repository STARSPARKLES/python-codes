#Code 1
from urllib.request import urlopen #importing urlopen function that uses to fetch url content
from bs4 import BeautifulSoup #importing beautiful soup for parse html content
from urllib.parse import urljoin #importing urljoin function that converts urls to absolute urls
URL = "https://www.codewithharry.com" # website url
webpage_url = urlopen(URL) #open url and fetch the content of web and store it in a webpage variable
parse_html = BeautifulSoup(webpage_url, 'html.parser') #beautifulsoup parse the content of html
for anchor_tags in parse_html.find_all('a'): # extract all anchor tags from html content
    link = anchor_tags.get('href')  # extract the value of the 'href' attribute from the anchor tag
    full_link = urljoin(URL, link)  # make the link absolute by joining it with the base URL
    if full_link.startswith(URL):   # checking if the link is an onsite link 
        print("Onsite Link:", full_link)  # Print the onsite link
    else:
        print("Offsite Link:", full_link)  # Print the offsite link
