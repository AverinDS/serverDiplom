import numpy
from keras.models import Sequential
from keras.layers import Dense, LSTM
import keras
from sklearn.preprocessing import MinMaxScaler


class MyNetwork:
    model = Sequential()
    max_length = 0
    look_back = 10
    y_train = numpy.array([])
    x_train = numpy.array([])
    x_train_list = []
    y_train_list = []
    scaler = MinMaxScaler(feature_range=(0, 1))

    def make_model(self, length_of_units):
        self.max_length = length_of_units

        self.model.add(LSTM(4, input_shape=(1, self.look_back)))
        self.model.add(Dense(1, activation='relu'))
        # self.model.add(Dense(12, input_shape=(1,)))
        # self.model.add(Dense(15, activation='relu'))
        # self.model.add(Dense(8, activation='relu'))
        # self.model.add(Dense(10, activation='relu'))
        # self.model.add(Dense(1, activation='sigmoid'))

        self.model.compile(loss="mean_squared_error", optimizer="adam")

    def fit(self, X, Y):
        X, Y = self.make_dataset(X, Y)
        X = numpy.reshape(X, (X.shape[0], 1, X.shape[1]))
        print(X)

        Y = self.scaler.fit_transform(Y.reshape(-1, 1))

        print (Y)
        self.model.fit(X, Y, epochs=50)

    def predict(self, X):
        predict_points = self.model.predict(self.make_dataset_X(X))
        predict_points = self.scaler.inverse_transform(predict_points)
        print(predict_points)
        return predict_points

    def make_dataset(self, X, Y):
        self.x_train_list = X
        self.y_train_list = Y

        dataX, dataY = [], []

        for i in range(len(X) - self.look_back - 1):
            dataX.append(X[i:(i + self.look_back), 0])
            dataY.append(Y[i + self.look_back, 0])
        self.y_train = numpy.array(dataY)
        self.x_train = numpy.array(dataX)
        return numpy.array(dataX), numpy.array(dataY)

    def make_dataset_X(self, X):
        dataX = []
        for i in range(self.look_back,0, -1):
            dataX.append(self.x_train[len(self.x_train)-1 - i])

        for i in range(len(X) - self.look_back - 1):
            dataX.append(X[i:(i + self.look_back), 0])

        dataX = numpy.array(dataX)
        # print(dataX)
        dataX = numpy.reshape(dataX, (dataX.shape[0], 1, dataX.shape[1]))
        # print(dataX)
        return dataX

