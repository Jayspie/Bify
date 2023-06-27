import spotipy
from spotipy.oauth2 import SpotifyOAuth
from info import *
import random
import pprint
import requests


scope="playlist-modify-public"
username=user_id
wowo_id='5vhMI6qUtzn8rDzJe7gSxv'
feels_id=""
weekly="37i9dQZEVXcNoaSgR2ccmo"

token=SpotifyOAuth(scope=scope, username=username)
spotifyobj=spotipy.Spotify(auth_manager=token)

a=spotifyobj.playlist_tracks(wowo_id)
i=0
list=[]
while True:
    tracks=a['items'][i]['track']['id'] 
    list.append(tracks)
    if i<99:
        i+=1
    elif i==99:
        break
while True:
    track=spotifyobj.track(random.choice(list))
    images=str(track['album']['images'][0]['url'])
    mp3=str(track['preview_url'])
    if mp3=='None':
        continue
    else:
        x=str(track['artists'][0]['name'])
        song=str(track['album']['name'])
        artist=x.replace(" ", "")
        print(images)
        print(mp3)
        print(artist)
        print(song)
        break

imurl = images
response = requests.get(imurl)
with open("image.jpg", "wb") as f:
    f.write(response.content)
mpurl = mp3
response = requests.get(mpurl)
with open("audio.mp3", "wb") as f:
    f.write(response.content)