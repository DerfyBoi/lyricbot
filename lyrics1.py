import requests
from bs4 import BeautifulSoup

#formatting user's inputs
def format(song, producer):
    global songFormat
    global producerFormat
    songFormat = song.replace(" ", "-")
    producerFormat = producer.replace(" ", "-")

#getting user's inputs
song = input("Song Name : ")
producer = input("Producer Name : ")
format(song, producer)

#entering user's inputs into website
try:
    url = "https://owldb.net/song/" + songFormat + "-" + producerFormat + "/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    #scraping lyrics from html with id romaji
    lyrics = soup.find(id="romaji").text.strip()
except ValueError:
    print("Song not found!")

#printing romaji lyrics
print("Source : " + url.lower() + "\n")
print("--------------------------------------------------------------------------------------------------------------------")
print(lyrics)
print("--------------------------------------------------------------------------------------------------------------------")
