import sys,os
path = '/Users/Povilas/Desktop/Final-Year-Project/'
actor_csv = path + 'moviesCSV/actorname_ID.csv'
djangopath = path + 'DjangoApp/'

sys.path.append(djangopath)
os.environ['DJANGO_SETTINGS_MODULE'] ='MovieRatingPredictor.settings'

from moviepredict.models import *

import csv

actor_nameDB = csv.reader(open(actor_csv), delimiter=',', mode='r',  encoding='utf8')
next(actor_nameDB, None)

for row in actor_nameDB:
    actor = Actor()
    actor.imdb_id = row[0]
    actor.name = row[1]
    actor.save()