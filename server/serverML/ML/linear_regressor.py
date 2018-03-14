from sklearn.linear_model import LinearRegression


class MyLinearRegression:
    regressor = LinearRegression()

    def fitting(self, Xdata, ydata):
        self.regressor.fit(Xdata, ydata)

    def get_predict(self, Xdata):
        return self.regressor.predict(Xdata)