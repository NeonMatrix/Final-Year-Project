import pandas as pd
import keras
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.utils import to_categorical 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn import preprocessing
import joblib

#creating scaler objects
budgetScaler = MinMaxScaler(feature_range=(0,1))
runtimeScaler = MinMaxScaler(feature_range=(0,1))
won_oscarsScaler = MinMaxScaler(feature_range=(0,1))
nominated_oscarsScaler = MinMaxScaler(feature_range=(0,1))
other_awards_wonScaler = MinMaxScaler(feature_range=(0,1))
other_awards_nominatedScaler = MinMaxScaler(feature_range=(0,1))
director_won_oscarScaler = MinMaxScaler(feature_range=(0,1))
director_nominated_oscarScaler = MinMaxScaler(feature_range=(0,1))
director_other_awards_wonScaler = MinMaxScaler(feature_range=(0,1))
director_other_awards_nominatedScaler = MinMaxScaler(feature_range=(0,1))

train_path = '/Users/Povilas/Desktop/Final-Year-Project/movieCSVs/movies.csv'
#train_path = '/home/paul/Desktop/Final-Year-Project/movieCSVs/movies.csv'
dataInputSize = 29

#load data from movies.csv into panda dataframe
dataset = pd.read_csv(train_path)
x_df = pd.DataFrame(dataset.iloc[:,1:dataInputSize])
y_df = pd.DataFrame(dataset.iloc[:,dataInputSize])

x_df['budget'] = budgetScaler.fit_transform(x_df[["budget"]])
x_df['runtime'] = runtimeScaler.fit_transform(x_df[["runtime"]])
x_df['won_oscars'] = won_oscarsScaler.fit_transform(x_df[["won_oscars"]])
x_df['nominated_oscars'] = nominated_oscarsScaler.fit_transform(x_df[["nominated_oscars"]])
x_df['other_awards_won'] = other_awards_wonScaler.fit_transform(x_df[["other_awards_won"]])
x_df['other_awards_nominated'] = other_awards_nominatedScaler.fit_transform(x_df[["other_awards_nominated"]])
x_df['director_won_oscar'] = director_won_oscarScaler.fit_transform(x_df[["director_won_oscar"]])
x_df['director_nominated_oscar'] = director_nominated_oscarScaler.fit_transform(x_df[["director_nominated_oscar"]])
x_df['director_other_awards_won'] = director_other_awards_wonScaler.fit_transform(x_df[["director_other_awards_won"]])
x_df['director_other_awards_nominated'] = director_other_awards_nominatedScaler.fit_transform(x_df[["director_other_awards_nominated"]])


# formats star ratings into array of categories i.e 3/10 stars = [0,0,1,0,0,0,0,0,0,0]
y_df = y_df.values.tolist()
y_df = np.array(y_df , dtype=int)
newRay = y_df.flatten()
#print(newRay)
expectedResult = to_categorical(newRay)
#print(expectedResult)
#print(x_df)

#the data is split into testing and training portions.
x_train, x_test, y_train, y_test = train_test_split(x_df, expectedResult, test_size=0.2, random_state=75)

# neural network layers set up here
model = Sequential()
model.add(Dense(100, activation='relu', input_dim=dataInputSize-1))
model.add(Dense(125, activation='relu'))
model.add(Dense(100, activation='relu'))
model.add(Dropout(0.25))
model.add(Dense(11, activation='softmax'))

# neural network is compiled
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# neural network is trained with the train data.
model.fit(x_train, y_train, batch_size=1, epochs=12)

# the accuratcy of the model is evalauted using testing portion of the trainig data.
score = model.evaluate(x_test, y_test)
print(f"Test Accuracy: {score[1]}")

# saving the prediction model and the scalers used
model.save('prediction_models/finalPredictionModel.h5')
joblib.dump(budgetScaler, 'scalers/budgetScaler.sav')
joblib.dump(runtimeScaler, 'scalers/runtimeScaler.sav') 
joblib.dump(won_oscarsScaler, 'scalers/won_oscarsScaler.sav') 
joblib.dump(nominated_oscarsScaler, 'scalers/nominated_oscarsScaler.sav') 
joblib.dump(other_awards_wonScaler, 'scalers/other_awards_wonScaler.sav') 
joblib.dump(other_awards_nominatedScaler, 'scalers/other_awards_nominatedScaler.sav') 
joblib.dump(director_won_oscarScaler, 'scalers/director_won_oscarScaler.sav') 
joblib.dump(director_nominated_oscarScaler, 'scalers/director_nominated_oscarScaler.sav') 
joblib.dump(director_other_awards_wonScaler, 'scalers/director_other_awards_wonScaler.sav') 
joblib.dump(director_other_awards_nominatedScaler, 'scalers/director_other_awards_nominatedScaler.sav')