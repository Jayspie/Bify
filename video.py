from moviepy.editor import *
from mutagen.mp3 import MP3
from spotify import*

# create the audio clip object
audio_clip = AudioFileClip("audio.mp3")

# create the image clip object
image_clip = ImageClip("image.jpg")

# use set_audio method from image clip to combine the audio with the image
video_clip = image_clip.set_audio(audio_clip)
video_clip.duration = audio_clip.duration
video_clip.fps = 24
video_clip.write_videofile('spot.mp4')