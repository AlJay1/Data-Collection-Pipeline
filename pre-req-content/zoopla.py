import requests
import bs4

from bs4 import BeautifulSoup

response = requests.get("https://www.zoopla.co.uk/new-homes/property/london/?q=London&results_sort=newest_listings&search_source=new-homes&page_size=25&view_type=list")
html = response.content
html = BeautifulSoup(html, 'html.parser')
#print(html)
houses = (html.find_all(name = 'div', attrs={'data-testid': 'regular-listings', 'class':'css-1itfubx e1artpxd0' }))
#print(houses)
home = (houses.find(name = 'p', attrs={'class':'c-bTssUX'}))
print(home)
for data in houses:
    tab = (data.prettify())
    
    #print(home)
