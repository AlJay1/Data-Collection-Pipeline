import requests
import bs4

from bs4 import BeautifulSoup
import requests # import the requests library
r = requests.get('http://pythonscraping.com/pages/page3.html') # make a HTTP GET request to this website
html_string = r.text # the text attribute of this response is the HTML as a string
soup = BeautifulSoup(html_string, 'html.parser') # Convert that into a BeautifulSoup object that contains methods to make the tag searcg easier

fish = soup.find(name='tr', attrs={'id': 'gift3', 'class': 'gift'}) # If it doesn't find anything it returns None

print(fish)
fish_row = fish.find_all('td') 
title = fish_row[0].text
description = fish_row[1].text
price = fish_row[2].text

print(title)
print(description)
print(price)

parrot = fish.find_next_sibling()
#print(parrot)

parrot_children = parrot.findChildren()
print(parrot_children)