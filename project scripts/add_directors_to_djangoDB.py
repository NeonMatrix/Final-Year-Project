from moviepredict.models import *
import csv

# this python script populated the Django Database with Director names and their IMDB IDs

dir_nameDB = csv.reader(open('/Users/Povilas/Desktop/Final-Year-Project/datasets/directorname_ID.csv', mode='r',  encoding='utf8'), delimiter=',')

for row in dir_nameDB:
    director = Director()
    director.imdb_id = row[0]
    director.name = row[1]
    print(row[0])
    director.save()