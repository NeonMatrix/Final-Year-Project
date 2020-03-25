from .models import *
import requests
from bs4 import BeautifulSoup
import pandas as pd
import keras
# import numpy as np
# from keras.models import Sequential
from keras.models import load_model
# from keras.layers import Dense
# from keras.layers import Dropout
# from keras.utils import to_categorical 
# from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing
# from sklearn.preprocessing import LabelEncoder
# from sklearn.preprocessing import OneHotEncoder
sc = StandardScaler()

def getActorID(actorName):
    a = Actor.objects.filter(name=actorName)
    if a:
        return a[0].imdb_id
    else:
        return 0

def getDirectorID(directorName):
    d = Director.objects.filter(name=directorName)
    if d:
        return d[0].imdb_id
    else:
        return 0

def getActorAwards(actorName):
    actorID = getActorID(actorName)
    if actorID == 0:
        return [0, 0, 0, 0]
    else:
        response = requests.get('https://www.imdb.com/name/' + actorID)
        soup = BeautifulSoup(response.text, 'lxml')
        awardsBlurb = soup.findAll('span', {"class" : 'awards-blurb'})

        numOscars = 0
        numNomOscars = 0
        numOtherWins = 0
        numOtherNoms = 0

        for award in awardsBlurb:
            if 'Won' in award.text and 'Oscar' in award.text:
                oscars = [int(s) for s in award.text.split() if s.isdigit()]
                #print('Owscar won ' + str(oscars[0]))
                numOscars = oscars[0]

            if 'Nominated' in award.text and 'Oscar' in award.text:
                nonimatedOscars = [int(s) for s in award.text.split() if s.isdigit()]
                #print('oscar nom ' + str(nonimatedOscars[0]))
                numNomOscars = nonimatedOscars[0]

            if 'win' in award.text and 'nomination' in award.text:
                otherAwards = [int(s) for s in award.text.split() if s.isdigit()]
                #print(str(otherAwards[0]) + ' ' + str(otherAwards[1]))
                #totOtherWins = totOtherWins + otherAwards[0]
                numOtherWins = otherAwards[0]
                #totOtherNoms = totOtherNoms + otherAwards[1]
                numOtherNoms = otherAwards[1]
            elif 'win' in award.text:
                otherAwards = [int(s) for s in award.text.split() if s.isdigit()]
                #print('wins ' + str(otherAwards[0]))
                #totOtherWins = totOtherWins + otherAwards[0]
                numOtherWins = otherAwards[0]
            elif 'nomination' in award.text:
                otherAwards = [int(s) for s in award.text.split() if s.isdigit()]
                #print('nominations ' + str( otherAwards[0]))
                #totOtherNoms = totOtherNoms + otherAwards[0]
                numOtherNoms = otherAwards[0]

        return [numOscars, numNomOscars, numOtherWins, numOtherNoms]

def getDirectorAwards(directorName):
    directorID = getDirectorID(directorName)
    if directorID == 0:
        return [0, 0, 0, 0]
    else:
        response = requests.get('https://www.imdb.com/name/' + directorID)
        soup = BeautifulSoup(response.text, 'lxml')
        awardsBlurb = soup.findAll('span', {"class" : 'awards-blurb'})

        numOscars = 0
        numNomOscars = 0
        numOtherWins = 0
        numOtherNoms = 0

        for award in awardsBlurb:
            if 'Won' in award.text and 'Oscar' in award.text:
                oscars = [int(s) for s in award.text.split() if s.isdigit()]
                #print('Owscar won ' + str(oscars[0]))
                numOscars = oscars[0]

            if 'Nominated' in award.text and 'Oscar' in award.text:
                nonimatedOscars = [int(s) for s in award.text.split() if s.isdigit()]
                #print('oscar nom ' + str(nonimatedOscars[0]))
                numNomOscars = nonimatedOscars[0]

            if 'win' in award.text and 'nomination' in award.text:
                otherAwards = [int(s) for s in award.text.split() if s.isdigit()]
                #print(str(otherAwards[0]) + ' ' + str(otherAwards[1]))
                #totOtherWins = totOtherWins + otherAwards[0]
                numOtherWins = otherAwards[0]
                #totOtherNoms = totOtherNoms + otherAwards[1]
                numOtherNoms = otherAwards[1]
            elif 'win' in award.text:
                otherAwards = [int(s) for s in award.text.split() if s.isdigit()]
                #print('wins ' + str(otherAwards[0]))
                #totOtherWins = totOtherWins + otherAwards[0]
                numOtherWins = otherAwards[0]
            elif 'nomination' in award.text:
                otherAwards = [int(s) for s in award.text.split() if s.isdigit()]
                #print('nominations ' + str( otherAwards[0]))
                #totOtherNoms = totOtherNoms + otherAwards[0]
                numOtherNoms = otherAwards[0]

        return [numOscars, numNomOscars, numOtherWins, numOtherNoms]

def preditRating(movieDetails):

    model = load_model('moviepredict/new_prediction_model.h5')

    dataset = { 'runtime': movieDetails[0],
                'budget': movieDetails[1],
                'Animation': movieDetails[2],
                'Action': movieDetails[3],
                'Adventure': movieDetails[4],
                'Comedy': movieDetails[5],
                'Crime': movieDetails[6],
                'Documentary': movieDetails[7],
                'Drama': movieDetails[8],
                'Family': movieDetails[9],
                'Fantasy': movieDetails[10],
                'History': movieDetails[11],
                'Horror': movieDetails[12],
                'Music': movieDetails[13],
                'Mystery': movieDetails[14],
                'Science Fiction': movieDetails[15],
                'Romance': movieDetails[16],
                'Thriller': movieDetails[17],
                'Western': movieDetails[18],
                'War': movieDetails[19],
                'won_oscars': movieDetails[20],
                'nominated_oscars': movieDetails[21],
                'other_awards_won': movieDetails[22],
                'other_awards_nominated': movieDetails[23],
                'director_won_oscar': movieDetails[24],
                'director_nominated_oscar': movieDetails[25],
                'director_other_awards_won': movieDetails[26],
                'director_other_awards_nominated': movieDetails[27]
    }

    #df = pd.DataFrame (dataset.items(), columns = ['runtime', 'budget', 'Animation', 'Action', 'Adventure', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy', 'History', 'Horror', 'Music', 'Mystery', 'Science Fiction', 'Romance', 'Thriller', 'Western', 'War', 'won_oscars', 'nominated_oscars', 'other_awards_won', 'other_awards_nominated', 'director_won_oscar', 'director_nominated_oscar', 'director_other_awards_won', 'director_other_awards_nominated'])
    df = pd.DataFrame ([dataset])

    df['budget'] = sc.fit_transform(df[["budget"]])
    df['runtime'] = sc.fit_transform(df[["runtime"]])
    df['won_oscars'] = sc.fit_transform(df[["won_oscars"]])
    df['nominated_oscars'] = sc.fit_transform(df[["nominated_oscars"]])
    df['other_awards_won'] = sc.fit_transform(df[["other_awards_won"]])
    df['other_awards_nominated'] = sc.fit_transform(df[["other_awards_nominated"]])
    # df['director_won_oscar'] = sc.fit_transform(df[["director_won_oscar"]])
    # df['director_nominated_oscar'] = sc.fit_transform(df[["director_nominated_oscar"]])
    # df['director_other_awards_won'] = sc.fit_transform(df[["director_other_awards_won"]])
    # df['director_other_awards_nominated'] = sc.fit_transform(df[["director_other_awards_nominated"]])

    prediction = model.predict(df)
    rating = 0
    for predic in prediction:
        highest = 0
        for i in range(len(predic)):
            if predic[i] > highest:
                highest = predic[i]
                rating = i

    return rating