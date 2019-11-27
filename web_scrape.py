import requests
from bs4 import BeautifulSoup
response = requests.get('https://www.imdb.com/title/tt0017136/')
# print(response.content)
#print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')
print(soup.find(class_='cast_list').find_all('a'))
# table = soup.find_all(class_='cast_list')
# print(table.find_all('a'))