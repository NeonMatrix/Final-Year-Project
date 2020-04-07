from moviepredict.models import *
import csv

# this python script populated the Django Database with Actors names and their IMDB IDs


actor_nameDB = csv.reader(open('/Users/Povilas/Desktop/Final-Year-Project/moviesCSV/actorname_ID.csv', mode='r',  encoding='utf8'), delimiter=',')

for i in range(857210):
	next(actor_nameDB, None)

for row in actor_nameDB:
    actor = Actor()
    actor.imdb_id = row[0]
    actor.name = row[1]
    actor.save()