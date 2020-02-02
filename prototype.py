import pandas as pd
import tensorflow as tf
import keras
import numpy as np
from keras.models import Sequential
from keras.layers import Dense 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing

sc = StandardScaler()

train_path = '/Users/Povilas/Desktop/Final-Year-Project/movies.csv'
dataset = pd.read_csv(train_path)
x_df = pd.DataFrame(dataset.iloc[:,1:21])
y_df = pd.DataFrame(dataset.iloc[:,21])

x_df['budget'] = sc.fit_transform(x_df[["budget"]])
x_df['runtime'] = sc.fit_transform(x_df[["runtime"]])
# x_df = sc.fit_transform(x_df)

y_df['movie rating'] = sc.fit_transform(y_df[["movie rating"]])
# x = dataset.iloc[:,1:21]
# y = dataset.iloc[:,21]

# x = np.array(x)
# x = x.reshape(-1, 1)
# x[1,:] = sc.fit_transform(x[1,:])

x_train, x_test, y_train, y_test = train_test_split(x_df, y_df, test_size=0.1, random_state=50)

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
model.add(Dense(100, activation='relu', input_dim=20))
model.add(Dense(100, activation='relu'))
model.add(Dense(100, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.fit(x_train, y_train, batch_size=300, epochs=10)



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