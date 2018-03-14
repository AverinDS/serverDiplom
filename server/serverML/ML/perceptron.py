from sklearn.linear_model import Perceptron


class MyPerceptron:
    perceptron = Perceptron(max_iter=15, tol=None)

    def fitting(self, x_data, y_data):
        self.perceptron.fit(x_data, y_data.ravel())

    def get_predict(self, x_data):
        return self.perceptron.predict(x_data)
