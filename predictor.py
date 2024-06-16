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

def generate_ion_charge(dataset_dictionary: pd.DataFrame):
    list_by_ion_charge = []
    for i in range(1, 401):
        compound_data = CompoundData(dataset_dictionary, "copper sulfate")
        compound_data.ion_mass = [10 * i, 10]
        input_data_fragment = compound_data.get_data(compound_data.from_grams_to_molar_conductivity(0.5))
        list_by_ion_charge.append(input_data_fragment)

    scaler = StandardScaler()
    scaler.fit(np.array(list_by_ion_charge))
    scaler.fit(list_by_ion_charge)
    return scaler.transform(list_by_ion_charge)

def generate_concentration(dataset_dictionary: pd.DataFrame):
    list_by_concentration = []
    for i in range(1, 401):
        compound_data = CompoundData(dataset_dictionary, "copper sulfate")
        input_data_fragment = compound_data.get_data(compound_data.from_grams_to_molar_conductivity(0.5 * i))
        list_by_concentration.append(input_data_fragment)
    
    scaler = StandardScaler()
    scaler.fit(np.array(list_by_concentration))
    return scaler.transform(list_by_concentration)

def split_dataset(dataset_trainable: DataSet, dataset_dictionary: pd.DataFrame):
    input_data_list = []
    output_data_list = []

    for solution in dataset_trainable.list_solutions():
        compound_data = CompoundData(dataset_dictionary, solution.solution_name)
        input_data_fragment = compound_data.get_data(compound_data.from_grams_to_molar_conductivity(solution.concentration))
        output_data_fragment = solution.get_averaged_conductivity()
        input_data_list.append(input_data_fragment)
        output_data_list.append(output_data_fragment)

    scaler = StandardScaler()
    scaler.fit(np.array(input_data_list))

    train_x, validation_x, train_y, validation_y = train_test_split(np.array(input_data_list), np.array(output_data_list), test_size=0.2, shuffle=True, random_state=34)

    scaled_train_x = scaler.transform(train_x)
    scaled_validation_x = scaler.transform(validation_x)

    return scaled_train_x, scaled_validation_x, train_y, validation_y

def deep_learning_solutions(dataset_trainable: DataSet, dataset_dictionary: pd.DataFrame):
    scaled_train_x, scaled_validation_x, train_y, validation_y = split_dataset(dataset_trainable, dataset_dictionary)

    print(scaled_train_x)

    model = Sequential()
    model.add(Dense(3, input_dim=4, activation='relu'))
    model.add(Dense(100, activation='sigmoid'))
    model.add(Dense(40, activation='relu'))
    model.add(Dense(1, activation='linear'))

    model.compile(loss='mean_squared_error', optimizer='adam', metrics=['mae'])
    model.summary()

    history = model.fit(scaled_train_x, train_y, validation_data=(scaled_validation_x, validation_y), epochs=800) # 105.8564

    print("Prediction, Actual, Offset")
    prediction_actual_offset = list(zip(model.predict(scaled_validation_x).reshape(1, -1).tolist()[0], list(validation_y)))
    prediction_actual_offset = list(zip(model.predict(scaled_validation_x).reshape(1, -1).tolist()[0], list(validation_y), list(map(lambda x: abs(x[0] - x[1]), prediction_actual_offset))))
    print(prediction_actual_offset)

    print("\nMax Offset")
    print(max(map(lambda x: abs(x[0] - x[1]), prediction_actual_offset)))
    pd.DataFrame(prediction_actual_offset).to_excel(excel_writer="./main.xlsx")

    plt.plot(range(1, 401), model.predict(generate_ion_charge(dataset_dictionary)))
    plt.xlim(right=1000)
    plt.show()

    # import shap

    # explainer = shap.KernelExplainer(model.predict, scaled_train_x)
    # shap_values = explainer.shap_values(scaled_train_x)
    # print(shap_values)
    # for i in range(8):
    #     feature_imp = np.mean(np.abs(shap_values[:, i]))
    #     print(f'{i}의 중요도 :', feature_imp)



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