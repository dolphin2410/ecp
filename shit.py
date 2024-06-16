import pandas as pd
from util.dataset import DataSet
from util.compound_data import CompoundData
from util.solution import Solution
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np
from matplotlib import pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import math

fake_x = np.array([0.1 * i for i in list(range(1, 401)) if i % 2 != 0])
fake_x = fake_x.reshape(-1, 1)

x = np.array([0.1 * i for i in list(range(1, 401)) if i % 2 == 0])
y = np.array([math.sqrt(i) for i in x])

x = x.reshape(-1, 1)
y = y.reshape(-1, 1)

scaler = StandardScaler()
scaler.fit(x)
x = scaler.transform(x)
fake_x = scaler.transform(fake_x)

x, a, y, b = train_test_split(x, y, test_size=0.4, shuffle=True, random_state=34)

model = Sequential()
model.add(Dense(256, input_dim=1, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(1, activation='linear'))

model.compile(loss='mean_squared_error', optimizer='adam', metrics=['mae'])
model.summary()

history = model.fit(x, y, validation_split=0.2, epochs=200) # 105.8564    training_loss = history.history['loss']

plt.plot(range(1, 401, 2), model.predict(fake_x))
plt.show()


training_loss = history.history['loss']
validation_loss = history.history['val_loss']
epochs = range(1, len(training_loss) + 1)
plt.plot(epochs, training_loss, 'y', label='Training Loss')
plt.plot(epochs, validation_loss, 'r', label='Validation Loss')
plt.title('Loss Function')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()