from sklearn.linear_model import Perceptron


class MyPerceptron:
    perceptron = Perceptron()

    def fittingPerceptron(self, Xdata, ydata):
        self.perceptron.fit(Xdata, ydata)

    def getPredictPerceptron(self, Xdata):
        return self.perceptron.predict(Xdata)
