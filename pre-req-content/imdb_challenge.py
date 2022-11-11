import requests
import bs4

from bs4 import BeautifulSoup

response = requests.get("https://www.imdb.com/title/tt0110912/?ref_=nv_sr_srsg_0")
html = response.content
html = BeautifulSoup(html, 'html.parser')
#print (html.title())
cast_list = (html.find_all(name='a', attrs={'data-testid': 'title-cast-item__actor', 'class':'sc-bfec09a1-1 gfeYgX' }))

for data in cast_list:
    cast = (data.prettify())
    #print(cast)
    actors = data.text
    #print(actors)
    link = data.get('href')
    #print(link)
    data_link = 'https://www.imdb.com'+link
    #print(data_link)

    res = requests.get(data_link)
    res = res.content
    #print(res)
    movie=BeautifulSoup(res,'html.parser')
    #print(movie)

    movie_date = movie.findAll(name='a',attrs={'class':"knownfor-ellipsis"})
    #print(movie_date)
    for movie_d in movie_date:
         
        known_for = movie_d.text

 

        Datas = {
            'name':actors,
            'link': link,
            'Movie':known_for
        }

    print (Datas)

            
          

    
    
     
    