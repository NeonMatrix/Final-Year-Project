import tensorflow as tf 
train_path = '/Users/Povilas/Desktop/Final-Year-Project/movies.csv'
trainset = tf.data.TextLineDataset(train_path).skip(1)

COLUMNS = ['imdb_id', 'runtime',
           'budget', 'reveune',
           'ratings']

FIELD_DEFAULTS = [[0.0], [0.0], [0.0], [0.0], [0]]
def _parse_line(line):
    # Decode the line into its fields
    fields = tf.io.decode_csv(line, FIELD_DEFAULTS)

    # Pack the result into a dictionary
    features = dict(zip(COLUMNS,fields))

    # Separate the label from the features
    label = features.pop('ratings')

    return features, label

trainset = trainset.map(_parse_line)
print(trainset)

model = tf.keras.models.Sequential([
  tf.keras.layers.Input(shape=(5)),
  tf.keras.layers.Dense(64, activation='relu'),
  tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(trainset, epochs=3)

# for x in trainset:
#     print(x)

# x = trainset.make_one_shot_iterator()
# x.get_next()