from .models import *
import requests
from bs4 import BeautifulSoup
import pandas as pd
import keras
from keras.models import load_model
from sklearn import preprocessing
import joblib

# find actor's IMDb ID from database 
def getActorID(actorName):
    a = Actor.objects.filter(name=actorName)
    if a:
        return a[0].imdb_id
    else:
        return 0

# find director's IMDb ID from database
def getDirectorID(directorName):
    d = Director.objects.filter(name=directorName)
    if d:
        return d[0].imdb_id
    else:
        return 0

def getActorAwards(actorName):

    #get actor IMDn ID from database
    actorID = getActorID(actorName)

    # If the actor was not found return 0 awards
    if actorID == 0:
        return [0, 0, 0, 0]
    else:
        # Web scrape for awards for the actor
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

    # get director IMDn ID from database
    directorID = getDirectorID(directorName)

    # If the director was not found return 0 awards
    if directorID == 0:
        return [0, 0, 0, 0]
    else:

        # Web scrape for awards for the director
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

# movie rating prediction fucntion
def preditRating(movieDetails):

    # load the prediction modle from file
    model = load_model('moviepredict/prediction_models/finalPredictionModel.h5')

    # load the svaed Scaler values from file
    budgetScaler = joblib.load('moviepredict/scalers/budgetScaler.sav')
    runtimeScaler = joblib.load('moviepredict/scalers/runtimeScaler.sav')
    won_oscarsScaler = joblib.load('moviepredict/scalers/won_oscarsScaler.sav')
    nominated_oscarsScaler = joblib.load('moviepredict/scalers/nominated_oscarsScaler.sav')
    other_awards_wonScaler = joblib.load('moviepredict/scalers/other_awards_wonScaler.sav')
    other_awards_nominatedScaler = joblib.load('moviepredict/scalers/other_awards_nominatedScaler.sav')
    director_won_oscarScaler = joblib.load('moviepredict/scalers/director_won_oscarScaler.sav')
    director_nominated_oscarScaler = joblib.load('moviepredict/scalers/director_nominated_oscarScaler.sav')
    director_other_awards_wonScaler = joblib.load('moviepredict/scalers/director_other_awards_wonScaler.sav')
    director_other_awards_nominatedScaler = joblib.load('moviepredict/scalers/director_other_awards_nominatedScaler.sav')

    # turn the array into python dictionary
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

    #turn python dictionary into a panda dataframe
    df = pd.DataFrame ([dataset])

    # Normalise and scale the data
    df['budget'] = budgetScaler.transform(df[["budget"]])
    df['runtime'] = runtimeScaler.transform(df[["runtime"]])
    df['won_oscars'] = won_oscarsScaler.transform(df[["won_oscars"]])
    df['nominated_oscars'] = nominated_oscarsScaler.transform(df[["nominated_oscars"]])
    df['other_awards_won'] = other_awards_wonScaler.transform(df[["other_awards_won"]])
    df['other_awards_nominated'] = other_awards_nominatedScaler.transform(df[["other_awards_nominated"]])
    df['director_won_oscar'] = director_won_oscarScaler.transform(df[["director_won_oscar"]])
    df['director_nominated_oscar'] = director_nominated_oscarScaler.transform(df[["director_nominated_oscar"]])
    df['director_other_awards_won'] = director_other_awards_wonScaler.transform(df[["director_other_awards_won"]])
    df['director_other_awards_nominated'] = director_other_awards_nominatedScaler.transform(df[["director_other_awards_nominated"]])

    # predict rating using the prediction model
    prediction = model.predict_classes(df)

    #return the predicted rating
    return int(prediction)