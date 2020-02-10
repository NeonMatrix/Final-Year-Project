import csv
import requests
from bs4 import BeautifulSoup

# with open('/Users/Povilas/Desktop/Final-Year-Project/datasets/imdb_movie_basics.tsv', mode='r',  encoding="utf8") as bmdb:
#         basics = csv.reader(bmdb, delimiter="\t", quotechar='"')

#/Users/Povilas/Desktop/Final-Year-Project/datasets/AllMoviesDetailsCleaned.csv
with open('/home/paul/Desktop/Final-Year-Project/datasets/AllMoviesDetailsCleaned.csv', mode='r',  encoding="utf8") as cmdb:
    clean_movie_db = csv.reader(cmdb, delimiter=";", quotechar='"')
    # for row in movie_db:
    #     print(row)

#basicsM = {'id': 'title'}
ratingsDic = {'id': 'ratings'}
voteCountDic = {'id': 'votes'}
extraMovieBudgetDic = {'id': 'budget'}
movieAwards = {'id': 'awards'}

# with open('/Users/Povilas/Desktop/Final-Year-Project/datasets/imdb_movie_basics.tsv', mode='r',  encoding="utf8") as bmdb:
#     basics = csv.reader(bmdb, delimiter="\t", quotechar='"')

with open('/home/paul/Desktop/Final-Year-Project/datasets/imdb_movie_ratings.tsv', mode='r',  encoding="utf8") as rmdb:
    ratings = csv.reader(rmdb, delimiter='\t')
    for row in ratings:
        ratingsDic[row[0]] =  row[1]
        voteCountDic[row[0]] = row[2]

with open('/home/paul/Desktop/Final-Year-Project/moviesCSV/movies_with_scrapped_budget.csv', mode='r',  encoding="utf8") as xtrabudget:
    extra = csv.reader(xtrabudget, delimiter=',')
    for row in extra:
        extraMovieBudgetDic[row[0]] = row[1]

with open('/home/paul/Desktop/Final-Year-Project/datasets/movies_with_actor_awards.csv', mode='r',  encoding="utf8") as awardsdb:
    awards = csv.reader(awardsdb, delimiter=',')
    for row in awards:
        movieAwards[row[0]] = [row[1], row[2], row[3], row[4]]

    #print(ratingsDic)
    with open('/home/paul/Desktop/Final-Year-Project/datasets/AllMoviesDetailsCleaned.csv', mode='r',  encoding="utf8") as cmdb:
        clean_movie_db = csv.reader(cmdb, delimiter=";", quotechar='"')

        with open('/home/paul/Desktop/Final-Year-Project/moviesCSV/movies.csv', 'w', newline='') as csvfile:
            fw = csv.writer(csvfile, delimiter=',',
                                    quotechar='"')
            # fw.writerow(['imdb_id', 'runtime', 'budget', 'reveune', 'ratings'])
            # fw.writerow(['imdb_id', 'runtime', 'budget', 'reveune', 'Animation', 'Action', 'Adventure', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy', 'History', 'Horror', 'Music', 'Mystery', 'Science Fiction','Romance','Thriller', 'Western', 'War', 'ratings'])
            fw.writerow(['imdb_id', 'runtime', 'budget', 'Animation', 'Action', 'Adventure', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy', 'History', 'Horror', 'Music', 'Mystery', 'Science Fiction','Romance','Thriller', 'Western', 'War', 'won_oscars', 'nominated_oscars', 'other_awards_won', 'other_awards_nominated', 'movie rating'])

            for row in clean_movie_db:
                #print(row)
                if row[3] == 'imdb_id':
                    pass
                elif row[3] != '' and row[12] != '' and row[12] != '0' and row[3] in ratingsDic and row[3] in movieAwards:
                    skip = False
                    if row[1] == '0':
                        if row[3] in extraMovieBudgetDic:
                            budget = extraMovieBudgetDic[row[3]]
                        else:
                            skip = True
                    else:
                        budget = row[1]
                        
                    if not skip:
                        animation = 0
                        action = 0
                        adevnture = 0 
                        comedy = 0 
                        crime = 0
                        documentary = 0 
                        drama = 0
                        family = 0
                        fantasy = 0
                        history = 0
                        horror = 0
                        music = 0
                        mystery = 0
                        scifi = 0 
                        romance = 0
                        thriller = 0
                        western = 0
                        war = 0
                        genres = row[2].split('|')
                        # print(genres)
                        for g in genres:
                            if(g=='Animation'):
                                animation=1
                            elif(g=='Action'):
                                action=1
                            elif(g=='Adventure'):
                                adevnture=1
                            elif(g=='Comedy'):
                                comedy=1
                            elif(g=='Crime'):
                                crime=1
                            elif(g=='Documentary'):
                                documentary=1
                            elif(g=='Drama'):
                                drama=1
                            elif(g=='Family'):
                                family=1
                            elif(g=='Fantasy'):
                                fantasy=1
                            elif(g=='History'):
                                history=1
                            elif(g=='Horror'):
                                horror=1
                            elif(g=='Music'):
                                music=1
                            elif(g=='Mystery'):
                                mystery=1
                            elif(g=='Science Fiction'):
                                scifi=1
                            elif(g=='Romance'):
                                romance=1
                            elif(g=='Thriller'):
                                thriller=1
                            elif(g=='Western'):
                                western=1
                            elif(g=='War'):
                                war=1

                        #ratingProduct = float(ratingsDic[row[3]]) * int(voteCountDic[row[3]])

                        fw.writerow([row[3], row[12], budget, animation, action, adevnture, comedy, crime, documentary, drama, family, fantasy, history, horror, music, mystery, scifi, romance, thriller, western, war, movieAwards[row[3]][0],movieAwards[row[3]][1],movieAwards[row[3]][2],movieAwards[row[3]][3], int(round(float(ratingsDic[row[3]])))])

print("done")

# with open('/Users/Povilas/Desktop/Final-Year-Project/datasets/AllMoviesDetailsCleaned.csv', mode='r',  encoding="utf8") as cmdb:
#         clean_movie_db = csv.reader(cmdb, delimiter=";", quotechar='"')
#         for row in clean_movie_db:
#             print(row[2])

# with open('/Users/Povilas/Desktop/Final-Year-Project/datasets/imdb_movie_basics.tsv', mode='r',  encoding="utf8") as rmdb:
#     moviebasics = csv.reader(rmdb, delimiter='\t')
#     for row in moviebasics:
#         print(row[8])

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
