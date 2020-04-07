import csv

# this python script parased through the AllMoviesDetailsCleaned.csv and 
# put all movies that didn't have a budget listed into a new CSV
# so then another python script would web scrape IMDb for the bugdet of those movies


with open('/Users/Povilas/Desktop/Final-Year-Project/datasets/AllMoviesDetailsCleaned.csv', mode='r',  encoding="utf8") as cmdb:
        clean_movie_db = csv.reader(cmdb, delimiter=";", quotechar='"')

        with open('/Users/Povilas/Desktop/Final-Year-Project/datasets/movies_without_budget.csv', 'w', newline='') as csvfile:
            fw = csv.writer(csvfile, delimiter=',',quotechar='"')

            for row in clean_movie_db:
                if row[3] == 'imdb_id':
                    pass
                elif row[1] == '0' and row[12] != '' and row[12] != '0' and row[3] != '':
                    fw.writerow([row[3]])
print('done')
