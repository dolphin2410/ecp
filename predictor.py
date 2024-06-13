import pandas as pd
from util.dataset import DataSet
from util.compound_data import CompoundData
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np
from matplotlib import pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

def deep_learning_solutions(dataset_trainable: DataSet, dataset_dictionary: pd.DataFrame):
    input_data_list = []
    output_data_list = []

    for solution in dataset_trainable.list_solutions():
        compound_data = CompoundData(dataset_dictionary, solution.solution_name)
        input_data_fragment = compound_data.get_data(compound_data.from_grams_to_molar_conductivity(solution.concentration))
        output_data_fragment = solution.get_averaged_conductivity()
        input_data_list.append(input_data_fragment)
        output_data_list.append(output_data_fragment)

    train_x, validation_x, train_y, validation_y = train_test_split(np.array(input_data_list), np.array(output_data_list), test_size=0.2, shuffle=True, random_state=34)
    scaler = StandardScaler()
    scaler.fit(train_x)

    scaled_train_x = scaler.transform(train_x)
    scaled_validation_x = scaler.transform(validation_x)

    model = Sequential()
    model.add(Dense(256, input_dim=8, activation='relu'))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(1, activation='linear'))

    model.compile(loss='mean_squared_error', optimizer='adam', metrics=['mae'])
    model.summary()

    history = model.fit(scaled_train_x, train_y, validation_split=0.2, epochs=359) # 105.8564

    print("Prediction, Actual")
    prediction_actual = list(zip(model.predict(scaled_train_x).reshape(1, -1).tolist()[0], list(train_y)))
    print(prediction_actual)
    print("\nMax Offset")
    print(max(map(lambda x: abs(x[0] - x[1]), prediction_actual)))

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