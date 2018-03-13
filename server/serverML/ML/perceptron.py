from sklearn.linear_model import Perceptron
import numpy as np


class MyPerceptron:
    perceptron = Perceptron(max_iter=15, tol=1)

    def make_data_from_json(self, request):
        x = []
        y = []

        for i in request:
            x.append(i['first'])
            y.append(i['second'])

        x = np.array(x).reshape(-1, 1)
        y = np.array(y).reshape(-1, 1)
        return x, y

    def fitting_perceptron(self, Xdata, ydata):
        self.perceptron.fit(Xdata, ydata)

    def get_predict_perceptron(self, Xdata):
        return self.perceptron.predict(Xdata)
