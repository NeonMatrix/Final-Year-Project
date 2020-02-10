import pandas as pd
import tensorflow as tf
import keras
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

sc = StandardScaler()

#train_path = '/Users/Povilas/Desktop/Final-Year-Project/moviesCSV/movies.csv'
train_path = '/home/paul/Desktop/Final-Year-Project/moviesCSV/movies.csv'
dataset = pd.read_csv(train_path)
x_df = pd.DataFrame(dataset.iloc[:,1:25])
y_df = pd.DataFrame(dataset.iloc[:,25])

x_df['budget'] = sc.fit_transform(x_df[["budget"]])
x_df['runtime'] = sc.fit_transform(x_df[["runtime"]])
x_df['won_oscars'] = sc.fit_transform(x_df[["won_oscars"]])
x_df['nominated_oscars'] = sc.fit_transform(x_df[["nominated_oscars"]])
x_df['other_awards_won'] = sc.fit_transform(x_df[["other_awards_won"]])
x_df['other_awards_nominated'] = sc.fit_transform(x_df[["other_awards_nominated"]])
# x_df = sc.fit_transform(x_df)


# le = LabelEncoder()
# int_encode = le.fit_transform(y_df)

# one_hot = OneHotEncoder(sparse=False)
# int_encoded = int_encode.reshape(len(int_encode) , 1)
# one_hot_encode = one_hot.fit_transform(int_encode)
y_df = y_df.values.tolist()
y_df = np.array(y_df , dtype=int)
newRay = y_df.flatten()
expectedResult = to_categorical(newRay)
print(expectedResult)
#* Val waz here

# to_categorical(y_df)
# print(y_df)


#y_df['movie rating'] = sc.fit_transform(y_df[["movie rating"]])
# x = dataset.iloc[:,1:21]
# y = dataset.iloc[:,21]

# x = np.array(x)
# x = x.reshape(-1, 1)
# x[1,:] = sc.fit_transform(x[1,:])

x_train, x_test, y_train, y_test = train_test_split(x_df, expectedResult, test_size=0.6, random_state=50)

# sc = StandardScaler()
# x_train = sc.fit_transform(x_train)
# x_test = sc.transform(x_test)

#y_train = sc.transform(y_train)
# x_train=(x_train-x_train.mean())/x_train.std()
# x = x_train[['budget']].values.astype(int)
# min_max_scaler = preprocessing.MinMaxScaler()
# x_scaled = min_max_scaler.fit_transform(x)
# x_train = pd.DataFrame(x_scaled)

# y_train=(y_train-y_train.mean())/y_train.std()
# y_train = y_train.reshape(-1, 1)

model = Sequential()
model.add(Dense(100, activation='relu', input_dim=24))
model.add(Dense(100, activation='relu'))
model.add(Dense(100, activation='relu'))
model.add(Dense(11, activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.fit(x_train, y_train, batch_size=10, epochs=100)

score = model.evaluate(x_test, y_test)
print(f"accuracy {score[1]}")


# trainset = tf.data.TextLineDataset(train_path).skip(1)

# COLUMNS = ['imdb_id', 'runtime',
#            'budget', 'reveune',
#            'ratings']

# FIELD_DEFAULTS = [[0.0], [0.0], [0.0], [0.0], [0]]
# def _parse_line(line):
#     # Decode the line into its fields
#     fields = tf.io.decode_csv(line, FIELD_DEFAULTS)

#     # Pack the result into a dictionary
#     features = dict(zip(COLUMNS,fields))

#     # Separate the label from the features
#     label = features.pop('ratings')

#     return features, label

# trainset = trainset.map(_parse_line)
# print(trainset)

# model = tf.keras.models.Sequential([
#   tf.keras.layers.Input(shape=(5)),
#   tf.keras.layers.Dense(64, activation='relu'),
#   tf.keras.layers.Dense(10, activation='softmax')
# ])

# model.compile(optimizer='adam',
#               loss='sparse_categorical_crossentropy',
#               metrics=['accuracy'])

# model.fit(trainset, epochs=3)

# # for x in trainset:
# #     print(x)

# # x = trainset.make_one_shot_iterator()
# # x.get_next()