from urllib.request import urlopen
from bs4 import BeautifulSoup
page = urlopen('https://www.instagram.com/musmeong/')
soup = BeautifulSoup(page)
tags=soup.findAll('img')
print(tags)
