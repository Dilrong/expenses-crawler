import requests
from bs4 import BeautifulSoup 

source = requests.get('https://naver.com').text
soup = BeautifulSoup(source, 'html.parser')
hostKey = soup.select('span')

index = 0 
for key in hostKey:
    index += 1
    print(str(index) + ', ' + key.text)
    if index >= 20:
        break