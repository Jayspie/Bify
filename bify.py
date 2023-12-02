from instagrapi import Client
from spotify import*
from video import*
import requests
from bs4 import BeautifulSoup

#autherization 
cl = Client()
cl.login(uSERNAME, pASSWORD)

#Webscraping google to find the artist instagram 
url = "https://www.google.com/search?q="+artist
html= requests.get(url)

soup = BeautifulSoup(html.text, 'html.parser')

a_element=soup.find_all('a')
a_string=str(a_element)
try: 

    separator = '>www.instagram.com › '
    separator2='</div>'

    front_del= a_string.split(separator, 1)[1]
    tag=front_del.split(separator2, 1)[0] 
except:
    pass

#Combining the song name artist name or instagram tag in the caption
if len(tag) == 0:
    capition=song+" - "+artist

elif len(tag) > 1:
    capition=song+" - @"+tag

#Delays the time when the post is going to be posted 
list=[60,7200,9000,3600,1,81,18000]
random_index = random.randint(0, len(list))
time.sleep(list[random_index])

#Post content to instagram
post=cl.album_upload(["Song_of_the_Day.jpg","spot.mp4"],capition)
