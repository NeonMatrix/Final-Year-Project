import pandas as pd
import keras
import numpy as np
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
sc = StandardScaler()

model = load_model('MovieRatingModel.h5')

train_path = '/Users/Povilas/Desktop/Final-Year-Project/moviesCSV/predict_movies.csv'
#train_path = '/home/paul/Desktop/Final-Year-Project/moviesCSV/predict_movies.csv'
dataInputSize = 29

dataset = pd.read_csv(train_path)
x_df = pd.DataFrame(dataset.iloc[:,1:dataInputSize])
y_df = pd.DataFrame(dataset.iloc[:,dataInputSize])

x_df['budget'] = sc.fit_transform(x_df[["budget"]])
x_df['runtime'] = sc.fit_transform(x_df[["runtime"]])
x_df['won_oscars'] = sc.fit_transform(x_df[["won_oscars"]])
x_df['nominated_oscars'] = sc.fit_transform(x_df[["nominated_oscars"]])
x_df['other_awards_won'] = sc.fit_transform(x_df[["other_awards_won"]])
x_df['other_awards_nominated'] = sc.fit_transform(x_df[["other_awards_nominated"]])
x_df['director_won_oscar'] = sc.fit_transform(x_df[["director_won_oscar"]])
x_df['director_nominated_oscar'] = sc.fit_transform(x_df[["director_nominated_oscar"]])
x_df['director_other_awards_won'] = sc.fit_transform(x_df[["director_other_awards_won"]])
x_df['director_other_awards_nominated'] = sc.fit_transform(x_df[["director_other_awards_nominated"]])
# print(y_df)
stars = y_df['movie rating']

prediction = model.predict(x_df)

#print(prediction)

predicted_rating = []
rating  = 0
for predic in prediction:
    highest = 0
    for i in range(len(predic)):
        if predic[i] > highest:
            highest = predic[i]
            rating = i
    predicted_rating.append(rating)
print(predicted_rating)

total = 0

for i in range(len(predicted_rating)):
    star_diff = predicted_rating[i] - stars[i]
    star_diff = abs(star_diff)
    star_diff =  star_diff * 10
    total = total + star_diff

eff_accu = 100 - total/len(predicted_rating)

print("Effective acuuracy: ", eff_accu)


# cats = [[111,95000000,0,0,0,1,0,0,1,1,0,0,0,0,0,0,0,0,0,2,0,195,462,1,0,32,53]]
# prediction = model.predict(cats)
# print('Cats prediction: ', prediction)
# print(predicted_rating)

# score = model.evaluate(x_test, y_test)
# print(f"Test Accuracy: {score[1]}")