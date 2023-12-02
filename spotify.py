import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from info import *
import random
import time
import requests

#autherization 
auth_manager = SpotifyClientCredentials(client_id,client_secret)
spotify = spotipy.Spotify(auth_manager=auth_manager)

#Open/Fixed varables 
i=0
list=[]
ids=[]
track_num=29

#Get data from playlist
a=spotify.playlist_tracks(weekly)

#Getting songs in the playlist Ids and putting them in a playlist
while True:
    tracks=a['items'][i]['track']['id']
    list.append(tracks)
    if i<track_num:
        i+=1
    elif i==track_num:
        break
time.sleep(15)


while True:
    
    #choosing a random Id(song) and getting information about the song
    random_index = random.randint(0, len(list))
    tRack=spotify.track(list[random_index])

    #Getting the song image, preview sound, name of the song, and the artist.
    images=str(tRack['album']['images'][0]['url'])
    mp3=str(tRack['preview_url'])
    if mp3=='None':
        continue
    else:
        x=str(tRack['artists'][0]['name'])
        song=str(tRack['name'])
        artist=x.replace(" ", "")
        break

#Downloading the image and preview sound
imurl = images
response = requests.get(imurl)
with open("image.jpg", "wb") as f:
    f.write(response.content)
mpurl = mp3
response = requests.get(mpurl)
with open("audio.mp3", "wb") as f:
    f.write(response.content)