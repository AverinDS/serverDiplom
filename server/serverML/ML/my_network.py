import numpy as np
import pandas as pd
from keras.callbacks import EarlyStopping
from keras.models import Sequential
from keras.layers import Dense, LSTM, BatchNormalization, LeakyReLU, Activation
from sklearn.preprocessing import MinMaxScaler


class MyNetwork:
    model = Sequential()
    input_dim_val = 50
    max_x = 1
    dataframe = pd.DataFrame()

    early_stopping = EarlyStopping(monitor='loss', patience=100, mode='auto')

    def make_model(self):
        self.model = Sequential()

        self.model = Sequential()
        self.model.add(Dense(64, input_dim=self.input_dim_val))
        self.model.add(BatchNormalization())
        self.model.add(LeakyReLU())
        self.model.add(Dense(16))
        self.model.add(BatchNormalization())
        self.model.add(LeakyReLU())
        self.model.add(Dense(1))
        self.model.add(Activation('linear'))
        self.model.compile(optimizer='Adadelta', loss='mean_squared_error')



    def fit(self, X, Y):
        self.dataframe = pd.DataFrame({'x': X.ravel(), 'y': Y.ravel()})
        x_train = self.make_dataset_x(self.dataframe['x'], self.input_dim_val)
        y_train = self.make_dataset_y(self.dataframe['y'], self.input_dim_val)
        self.dataframe['y'] = self.dataframe['y'].rolling(int(len(Y) / 30), win_type=None, min_periods=1).mean()
        self.max_x = max(self.dataframe['x'])
        self.model.fit(x_train, y_train, epochs=200, callbacks=[self.early_stopping])
        print("FITTING COMPLETE!")


    def predict(self):
        # x_test = self.makePredictDataset(self.dataframe['x'],
        #                                  [i for i in range(self.max_x, self.max_x + 3 * self.input_dim_val)])
        x_test = self.makePredictDataset([],
                                         [i for i in range(self.max_x, self.max_x + 3 * self.input_dim_val)])
        x_test_one_dataset = x_test

        x_test = self.make_dataset_x(x_test, self.input_dim_val)
        y_predict = self.model.predict(x_test)
        return np.array(x_test_one_dataset[:len(y_predict)]), np.array(y_predict)




    def make_dataset_x(self, x, size):
        new_dataset = []
        checkNotEnough = False
        for i in range(len(x) - 1, 0, -1):
            temp = []
            for j in range(size):
                if (i - j) >= 0:
                    temp.append(x[i - j])
                else:
                    checkNotEnough = True
                    break
            if not checkNotEnough:
                new_dataset.append(temp)

            new_dataset.reverse()
        return np.array(new_dataset)

    def make_dataset_y(self, y, size):
        return np.array(y[size - 1:])

    def makePredictDataset(self, x, x1):
        data = []
        for i in x:
            data.append(i)
        for i in x1:
            data.append(i)
        return data

