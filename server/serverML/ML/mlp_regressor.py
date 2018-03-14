from sklearn.neural_network import MLPRegressor


class MyMLPRegressor:
    regressor = MLPRegressor()

    def fitting(self, x_data, y_data):
        self.regressor.fit(x_data, y_data)

    def get_predict(self, x_data):
        return self.regressor.predict(x_data)
