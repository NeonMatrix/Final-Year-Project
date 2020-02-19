import threading
from queue import Queue
import requests
from bs4 import BeautifulSoup
import csv

path = '/home/paul/Desktop/Final-Year-Project/'
# path = '/Users/Povilas/Desktop/Final-Year-Project'

response = requests.get('https://www.imdb.com/title/tt1853728')
soup = BeautifulSoup(response.text, 'lxml')
print(soup)
relaseDate = soup.findAll("div", {"class" : "title_wrapper"})
print(relaseDate)

# with open(path + 'moviesCSV/testmovies.csv', mode='r',  encoding="utf8") as cmdb:
#     movies = csv.reader(cmdb, delimiter=",", quotechar='"')

#     with open(path + 'datasets/testdate.csv', 'w', newline='') as csvfile:
#         fw = csv.writer(csvfile, delimiter=',',quotechar='"')