import pandas as pd
import keras
import numpy as np
from numpy import array
from keras.models import Sequential
from keras.models import load_model
from keras.layers import Dense
from keras.layers import Dropout
from keras.utils import to_categorical 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
#from sklearn.externals import joblib
import joblib 

budgetScaler = joblib.load('scalers/budgetScaler.sav') 
runtimeScaler = joblib.load('scalers/runtimeScaler.sav') 
won_oscarsScaler = joblib.load('scalers/won_oscarsScaler.sav') 
nominated_oscarsScaler = joblib.load('scalers/nominated_oscarsScaler.sav') 
other_awards_wonScaler = joblib.load('scalers/other_awards_wonScaler.sav') 
other_awards_nominatedScaler = joblib.load('scalers/other_awards_nominatedScaler.sav') 
director_won_oscarScaler = joblib.load('scalers/director_won_oscarScaler.sav') 
director_nominated_oscarScaler = joblib.load('scalers/director_nominated_oscarScaler.sav') 
director_other_awards_wonScaler = joblib.load('scalers/director_other_awards_wonScaler.sav') 
director_other_awards_nominatedScaler = joblib.load('scalers/director_other_awards_nominatedScaler.sav') 

model = load_model('prediction_models/minMaxPredictionModel.h5')

train_path = '/Users/Povilas/Desktop/Final-Year-Project/moviesCSV/predict_movies.csv'
#train_path = '/home/paul/Desktop/Final-Year-Project/moviesCSV/predict_movies.csv'
dataInputSize = 29 

dataset = pd.read_csv(train_path)
# print(dataset.loc[0])

x_df = pd.DataFrame(dataset.iloc[:,1:dataInputSize])
y_df = pd.DataFrame(dataset.iloc[:,dataInputSize])

x_df['budget'] = budgetScaler.transform(x_df[["budget"]])
x_df['runtime'] = runtimeScaler.transform(x_df[["runtime"]])
x_df['won_oscars'] = won_oscarsScaler.transform(x_df[["won_oscars"]])
x_df['nominated_oscars'] = nominated_oscarsScaler.transform(x_df[["nominated_oscars"]])
x_df['other_awards_won'] = other_awards_wonScaler.transform(x_df[["other_awards_won"]])
x_df['other_awards_nominated'] = other_awards_nominatedScaler.transform(x_df[["other_awards_nominated"]])
x_df['director_won_oscar'] = director_won_oscarScaler.transform(x_df[["director_won_oscar"]])
x_df['director_nominated_oscar'] = director_nominated_oscarScaler.transform(x_df[["director_nominated_oscar"]])
x_df['director_other_awards_won'] = director_other_awards_wonScaler.transform(x_df[["director_other_awards_won"]])
x_df['director_other_awards_nominated'] = director_other_awards_nominatedScaler.transform(x_df[["director_other_awards_nominated"]])
# print(y_df)
stars = y_df['movie rating']


prediction = model.predict_classes(x_df)

print(prediction)

total = 0
ten = 0
nine = 0 
eight = 0
seven = 0
six = 0
five = 0
four = 0
three = 0
two = 0
one = 0

for i in range(len(prediction)):
    star_diff = prediction[i] - stars[i]
    if(prediction[i] == 10):
        #print(dataset['imdb_id'].loc[i])
        ten += 1
    if(prediction[i] == 9):
        #print(dataset['imdb_id'].loc[i])
        nine += 1
    if(prediction[i] == 8):
        #print(dataset['imdb_id'].loc[i])
        eight += 1
    if(prediction[i] == 7):
        #print(dataset['imdb_id'].loc[i])
        seven += 1
    if(prediction[i] == 6):
        #print(dataset['imdb_id'].loc[i])
        six += 1
    if(prediction[i] == 5):
        #print(dataset['imdb_id'].loc[i])
        five += 1
    if(prediction[i] == 4):
        #print(dataset['imdb_id'].loc[i])
        four += 1
    if(prediction[i] == 3):
        #print(dataset['imdb_id'].loc[i])
        three += 1
    if(prediction[i] == 2):
        #print(dataset['imdb_id'].loc[i])
        two += 1
    if(prediction[i] == 1):
        #print(dataset['imdb_id'].loc[i])
        one += 1

    star_diff = abs(star_diff)
    star_diff =  star_diff * 10
    total = total + star_diff

eff_accu = 100 - total/len(prediction)

print("Effective acuuracy: ", eff_accu)

print("Ten: ", ten)
print("Nine: ", nine)
print("Eight: ", eight)
print("Seven: ", seven)
print("Six: ", six)
print("Five: ", five)
print("Four: ", four)
print("Three: ", three)
print("Two: ", two)
print("One: ", one)