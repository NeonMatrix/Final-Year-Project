import threading
from queue import Queue
import requests
from bs4 import BeautifulSoup
import csv

q = Queue()
lock = threading.Lock()
run = True

with open('/Users/Povilas/Desktop/Final-Year-Project/datasets/movies_without_budget.csv', mode='r',  encoding="utf8") as cmdb:
        movies = csv.reader(cmdb, delimiter=";", quotechar='"')

        with open('/Users/Povilas/Desktop/Final-Year-Project/datasets/DEMO_movies_with_scrapped_budget.csv', 'w', newline='') as csvfile:
            fw = csv.writer(csvfile, delimiter=',',quotechar='"')

            def getBudgetFromIMDB(movieID):
                try:
                    url = 'https://www.imdb.com/title/' + movieID
                    # make the request to IDMb websoite to get the HTML for the movie page
                    response = requests.get(url)
                    # using BeautifulSoup find the location of the budget in the HTML page
                    soup = BeautifulSoup(response.text, 'lxml')
                    budget_html = soup.find(text='Budget:').parent.parent
                    budget_rawval = budget_html.find('h4').next_sibling
                    budget = ''
                    #extracting the number value from the tags that hold the budget for the movie
                    for n in budget_rawval:
                        if(n.isdigit()):
                            budget = budget + n
                    #which thread synchronisation, add the movie budget to the dataset
                    with lock:
                        fw.writerow([movieID, budget])
                        print('Added budget for ' + movieID)

                except AttributeError:
                    #print("No budget found for " + movieID)
                    pass

            # defintion of the thread
            # gets movie ID from the queue and makes the HTML request for it
            def threader():
                while run:
                    movieID = q.get()
                    getBudgetFromIMDB(movieID)
                    q.task_done()

            # initalsing 256 threads
            for x in range(256):
                t = threading.Thread(target = threader)
                t.daemon = True
                t.start()

            #loop to place all movie IDs of movies without budget to the queue
            for row in movies:
                q.put(row[0])
                #print(row[0])

            q.join()
            run = False

print('done')