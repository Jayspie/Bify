from instagrapi import Client

ACCOUNT_USERNAME="_b1fy"
ACCOUNT_PASSWORD='892alpha!@#6A'

cl = Client()
cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)

#media = cl.photo_upload(
 #   path="BIFY.jpg",
  #  caption="This is a test but welcome to BIFY's profile")
cl.photo_upload_to_story(path="BIFY.jpg")