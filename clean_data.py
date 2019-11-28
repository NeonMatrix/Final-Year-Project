import csv
import requests
from bs4 import BeautifulSoup

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
            # fw.writerow(['imdb_id', 'runtime', 'budget', 'reveune', 'ratings'])
            # fw.writerow(['imdb_id', 'runtime', 'budget', 'reveune', 'Animation', 'Action', 'Adventure', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy', 'History', 'Horror', 'Music', 'Mystery', 'Science Fiction','Romance','Thriller', 'Western', 'War', 'ratings'])
            fw.writerow(['imdb_id', 'runtime', 'budget', 'Animation', 'Action', 'Adventure', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy', 'History', 'Horror', 'Music', 'Mystery', 'Science Fiction','Romance','Thriller', 'Western', 'War', 'ratings'])

            for row in clean_movie_db:
                #print(row)
                if row[3] == 'imdb_id':
                    pass
                elif row[3] != '' and row[12] != '' and row[12] != '0' and row[3] in ratingsDic:
                    skip = False
                    if row[1] == '0':
                        try:
                            print(row[3])
                            url = 'https://www.imdb.com/title/' + row[3]
                            response = requests.get(url)
                            soup = BeautifulSoup(response.text, 'lxml')
                            budget_html = soup.find(text='Budget:').parent.parent
                            budget_rawval = budget_html.find('h4').next_sibling
                            budget = ''
                            for n in budget_rawval:
                                if(n.isdigit()):
                                    budget = budget + n
                            row[1] = budget
                        except AttributeError:
                            print("No budget found for " + row[3])
                            skip = True
                        
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

                        fw.writerow([row[3], row[12], row[1], animation, action, adevnture, comedy, crime, documentary, drama, family, fantasy, history, horror, music, mystery, scifi, romance, thriller, western, war, ratingsDic[row[3]]])

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
