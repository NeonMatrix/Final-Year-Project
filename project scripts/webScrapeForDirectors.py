import threading
from queue import Queue
import requests
from bs4 import BeautifulSoup
import csv

# python script to web scraoe for Direcor Oscars/Awards and nominations


q = Queue()
lock = threading.Lock()
run = True

# /Users/Povilas/Desktop/Final-Year-Project/datasets/director_awards.csv

with open('/Users/Povilas/Desktop/Final-Year-Project/moviesCSV/movies.csv', mode='r',  encoding="utf8") as cmdb:
    movies = csv.reader(cmdb, delimiter=",", quotechar='"')

    with open('/Users/Povilas/Desktop/Final-Year-Project/datasets/director_awards2.csv', 'w', newline='') as csvfile:
        fw = csv.writer(csvfile, delimiter=',',quotechar='"')

        def getActorAwards(movieID):
            try:
                directorLinks = []
                totOscars = 0
                totOscarsNoms = 0
                totOtherWins = 0 
                totOtherNoms = 0

                response = requests.get('https://www.imdb.com/title/' + movieID)
                soup = BeautifulSoup(response.text, 'lxml')
                try:
                    cred_summary = soup.find(text='Director:').parent.next_sibling.next_sibling
                    directorLinks.append(cred_summary.get('href'))
                except AttributeError as e:
                    try:
                        # print('Looking for multiple directors in ' + movieID)
                        cred_summary = soup.find(text='Directors:').parent.parent
                        directors = cred_summary.findAll('a')
                        for link in directors:
                            directorLinks.append(link.get('href'))
                    except AttributeError as e:
                            print("Oppise doopsie on " + movieID)
                            print(e)
                            #traceback.print_exc()
                            pass

                for director in directorLinks:
                    response = requests.get('https://www.imdb.com/' + director)
                    soup = BeautifulSoup(response.text, 'lxml')
                    awardsBlurb = soup.findAll('span', {"class" : 'awards-blurb'})
                    #print(awardsBlurb[0].text)

                    for award in awardsBlurb:
                        if 'Won' in award.text and 'Oscar' in award.text:
                            oscars = [int(s) for s in award.text.split() if s.isdigit()]
                            #print('Owscar won ' + str(oscars[0]))
                            totOscars = totOscars + oscars[0]

                        if 'Nominated' in award.text and 'Oscar' in award.text:
                            nonimatedOscars = [int(s) for s in award.text.split() if s.isdigit()]
                            #print('oscar nom ' + str(nonimatedOscars[0]))
                            totOscarsNoms = totOscarsNoms + nonimatedOscars[0]

                        if 'win' in award.text and 'nomination' in award.text:
                            otherAwards = [int(s) for s in award.text.split() if s.isdigit()]
                            #print(str(otherAwards[0]) + ' ' + str(otherAwards[1]))
                            totOtherWins =  totOtherWins + otherAwards[0]
                            totOtherNoms =  totOtherNoms + otherAwards[1]
                        elif 'win' in award.text:
                            otherAwards = [int(s) for s in award.text.split() if s.isdigit()]
                            #print('wins ' + str(otherAwards[0]))
                            totOtherWins = otherAwards[0]
                        elif 'nomination' in award.text:
                            otherAwards = [int(s) for s in award.text.split() if s.isdigit()]
                            #print('nominations ' + str( otherAwards[0]))
                            totOtherNoms = otherAwards[0]

                with lock:
                    fw.writerow([movieID, totOscars, totOscarsNoms, totOtherWins, totOtherNoms])
                    print(movieID + ' Total Oscars: ' + str(totOscars)  + '  Oscar nominations: ' + str(totOscarsNoms) + '  total other awards: ' + str(totOtherWins)  + '  total other nominations: ' + str(totOtherNoms))

            except AttributeError as e:
                            print("Oppise doopsie on " + movieID)
                            print(e)
                            #traceback.print_exc()
                            pass

        def threader():
            while run:
                movieID = q.get()
                getActorAwards(movieID)
                q.task_done()

        for x in range(200):
            t = threading.Thread(target = threader)
            t.daemon = True
            t.start()

        for row in movies:
            q.put(row[0])
            #print(row[0])

        q.join()
        run = False

print("Done")