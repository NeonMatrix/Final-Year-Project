import csv

# with open('/Users/Povilas/Desktop/Final-Year-Project/datasets/imdb_movie_basics.tsv', mode='r',  encoding="utf8") as bmdb:
#         basics = csv.reader(bmdb, delimiter="\t", quotechar='"')

with open('/Users/Povilas/Desktop/Final-Year-Project/datasets/AllMoviesDetailsCleaned.csv', mode='r',  encoding="utf8") as cmdb:
    clean_movie_db = csv.reader(cmdb, delimiter=";", quotechar='"')
    # for row in movie_db:
    #     print(row)

#basicsM = {'id': 'title'}
ratingsDic = {'id': 'ratings'}

# with open('/Users/Povilas/Desktop/Final-Year-Project/datasets/imdb_movie_basics.tsv', mode='r',  encoding="utf8") as bmdb:
#     basics = csv.reader(bmdb, delimiter="\t", quotechar='"')

with open('/Users/Povilas/Desktop/Final-Year-Project/datasets/imdb_movie_ratings.tsv', mode='r',  encoding="utf8") as rmdb:
    ratings = csv.reader(rmdb, delimiter='\t')
    for row in ratings:
        ratingsDic[row[0]] =  row[1]

    #print(ratingsDic)
    with open('/Users/Povilas/Desktop/Final-Year-Project/datasets/AllMoviesDetailsCleaned.csv', mode='r',  encoding="utf8") as cmdb:
        clean_movie_db = csv.reader(cmdb, delimiter=";", quotechar='"')

        with open('/Users/Povilas/Desktop/Final-Year-Project/movies.csv', 'w', newline='') as csvfile:
            fw = csv.writer(csvfile, delimiter=',',
                                    quotechar='"')
            fw.writerow(['imdb_id', 'runtime', 'budget', 'reveune', 'ratings'])

            for row in clean_movie_db:
                #print(row)
                if row[3] == 'imdb_id':
                    pass
                elif row[3] != '' and row[1] != '0' and row[11] != '0' and row[12] != '' and row[12] != '0' and row[3] in ratingsDic:
                    fw.writerow([row[3], row[12], row[1], row[11], ratingsDic[row[3]]])

print("done")
# with open('movies.csv', 'w') as csvfile:
#     fw = csv.writer(csvfile, delimiter=',',
#                             quotechar='"')
#     fw.writerow(['imdb_id', 'runtime', 'budget', 'reveune', 'ratings'])

# for row in basics:
#     basicsM[row[0]] =  row[2]

# for row in ratings:
#     ratingsDic[row[0]] =  row[1]  

# for row in clean_movie_db:
#     if row['budget'] != 0 and row['revenue'] != 0:
#         fw.writerow([row[3], row[12], row[1], row[11], ratingsDic[row[3]]])

# for row in basics:
#     basicsM[row[0]] =  row[2]    

#print(basicsM)
# for row in db1:
#     for row1 in basics

# with open('/Users/Povilas/Desktop/Final-Year-Project/datasets/AllMoviesDetailsCleaned.csv', mode='r',  encoding="utf8") as db1:
#     movie_db = csv.reader(db1, delimiter=";", quotechar='"')
#     for row in movie_db:
