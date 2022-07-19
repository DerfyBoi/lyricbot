import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

#chromium options to disable GUI
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1080,1080")

search = input("Search artist/song: ")

#putting search term in browser search
driver = webdriver.Chrome('C:\webdrivers/chromedriver.exe',chrome_options=options)
driver.get("https://owldb.net")
inputElement = driver.find_element_by_id("search")
inputElement.send_keys(search,Keys.ENTER)

#getting lyrics
page = requests.get(driver.current_url)
soup = BeautifulSoup(page.content, "html.parser")
songs = soup.find('div',class_='row pt-3').text.strip()

#printing romaji lyrics
print("--------------------------------------------------------------------------------------------------------------------")
print(songs)
print("--------------------------------------------------------------------------------------------------------------------")

#get songs into array
#get number of songs as index + 1
#select songs with index
#click into song depending on number
#strip lyrics
