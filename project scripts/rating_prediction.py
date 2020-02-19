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

#train_path = '/Users/Povilas/Desktop/Final-Year-Project/moviesCSV/movies.csv'
train_path = '/home/paul/Desktop/Final-Year-Project/moviesCSV/predict_movies.csv'
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

print(x_df)

prediction = model.predict(x_df)
print(prediction)
# score = model.evaluate(x_test, y_test)
# print(f"Test Accuracy: {score[1]}")