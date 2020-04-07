import csv

path = '/Users/Povilas/Desktop/Final-Year-Project/'

# This python script extracted the Actors and Directors from IMDB's dataset of all 
# people that are recorded within IMDB website.

with open(path + 'datasets/imdb_name_data.tsv', mode='r',  encoding="utf8") as namedb:
    actor_nameDB = csv.reader(namedb, delimiter="\t")

    with open(path + 'moviesCSV/actorname_ID.csv', mode='w', newline='', encoding="utf8") as new_actorDB:
            fw_actor = csv.writer(new_actorDB, delimiter=',')

            with open(path + 'moviesCSV/directorname_ID.csv', mode='w', newline='', encoding="utf8") as new_directorDB:
                fw_director = csv.writer(new_directorDB, delimiter=',')
        
                fw_actor.writerow(['imdb_nameID', 'name'])
                fw_director.writerow(['imdb_nameID', 'name'])

                for row in actor_nameDB:
                    if 'actor' in row[4] or 'actress' in row[4]:
                        fw_actor.writerow([row[0], row[1]])
                    if 'director' in row[4]:
                        fw_director.writerow([row[0], row[1]])

print('done')