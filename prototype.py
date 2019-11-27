import pandas as pd
import tensorflow as tf
import keras
from keras.models import Sequential
from keras.layers import Dense 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
train_path = '/Users/Povilas/Desktop/Final-Year-Project/movies.csv'

dataset = pd.read_csv(train_path)
x = dataset.iloc[:,1:21]
y = dataset.iloc[:,21]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=0)

sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

model = Sequential()
model.add(Dense(150, activation='relu', input_dim=20))
model.add(Dense(150, activation='relu'))
model.add(Dense(150, activation='relu'))
# model.add(Dense(150, activation='relu'))
# model.add(Dense(150, activation='relu'))
# model.add(Dense(150, activation='relu'))
# model.add(Dense(150, activation='relu'))
model.add(Dense(1, activation='relu'))

# model.add(Dense(21, activation='relu', kernel_initializer='uniform', input_dim=21))
# model.add(Dense(21, activation='relu', kernel_initializer='uniform'))
# model.add(Dense(1, activation='softmax', kernel_initializer='uniform'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.fit(x_train, y_train, batch_size=150, epochs=50)



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