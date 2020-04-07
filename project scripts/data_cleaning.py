import csv
import requests
from bs4 import BeautifulSoup

#Path to where the project is located
path = '/Users/Povilas/Desktop/Final-Year-Project/'

# Dictionaires to hold imporant data to be merged with later
ratingsDic = {'id': 'ratings'}
voteCountDic = {'id': 'votes'}
extraMovieBudgetDic = {'id': 'budget'}
movieAwards = {'id': 'awards'}
directorAwards = {'id' : 'awards'}

# Get all movie ratings from imdb dataset into a dictionary
with open(path + 'datasets/imdb_movie_ratings.tsv', mode='r',  encoding="utf8") as rmdb:
    ratings = csv.reader(rmdb, delimiter='\t')
    for row in ratings:
        ratingsDic[row[0]] =  row[1]
        voteCountDic[row[0]] = row[2]


# Get all movie budgets from movies with webscraped budgets into a dictionary
with open(path + 'movieCSVs/movies_with_scrapped_budget.csv', mode='r',  encoding="utf8") as xtrabudget:
    extra = csv.reader(xtrabudget, delimiter=',')
    for row in extra:
        extraMovieBudgetDic[row[0]] = row[1]

# Get all actors awards into the dictionary from dataset with webscarped actor award data
with open(path + 'datasets/movies_with_actor_awards.csv', mode='r',  encoding="utf8") as awardsdb:
    awards = csv.reader(awardsdb, delimiter=',')
    for row in awards:
        movieAwards[row[0]] = [row[1], row[2], row[3], row[4]]

# Get all director awards into the dictionary from dataset with webscarped director award data
with open(path + 'datasets/director_awards.csv', mode='r',  encoding="utf8") as rmdb:
    ratings = csv.reader(rmdb, delimiter=',')
    for row in ratings:
        directorAwards[row[0]] = [row[1], row[2], row[3], row[4]]

#Merging all the datasets, imdb data, webscraped data and the main dataset from keggle into one movies.csv file
with open(path + 'datasets/AllMoviesDetailsCleaned.csv', mode='r',  encoding="utf8") as cmdb:
    clean_movie_db = csv.reader(cmdb, delimiter=";", quotechar='"')

    # creating movies.csv file
    with open(path + 'movieCSVs/movies.csv', 'w', newline='') as csvfile:
        fw = csv.writer(csvfile, delimiter=',',
                                quotechar='"')
        # wrting the header
        fw.writerow(['imdb_id', 'runtime', 'budget', 'Animation', 'Action', 'Adventure', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy', 'History', 'Horror', 'Music', 'Mystery', 'Science Fiction','Romance','Thriller', 'Western', 'War', 'won_oscars', 'nominated_oscars', 'other_awards_won', 'other_awards_nominated', 'director_won_oscar', 'director_nominated_oscar', 'director_other_awards_won', 'director_other_awards_nominated','movie rating'])

        #main loop of merging the data and writing it to movies.csv
        for row in clean_movie_db:
            #print(row)
            if row[3] == 'imdb_id':
                pass
            elif row[3] != '' and row[12] != '' and row[12] != '0' and row[3] in ratingsDic and row[3] in movieAwards and row[3] in directorAwards:
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

                    # quick pre-processing by encoding the movie genre into a binary represation
                    # genre are going to reoresent by an array of 1s and 0s
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

                    fw.writerow([row[3], row[12], budget, animation, action, adevnture, comedy, crime, documentary, drama, family, fantasy, history, horror, music, mystery, scifi, romance, thriller, western, war, movieAwards[row[3]][0],movieAwards[row[3]][1],movieAwards[row[3]][2],movieAwards[row[3]][3], directorAwards[row[3]][0], directorAwards[row[3]][1], directorAwards[row[3]][2], directorAwards[row[3]][3], int(round(float(ratingsDic[row[3]])))])

print("done")