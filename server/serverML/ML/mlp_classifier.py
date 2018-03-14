from sklearn.neural_network import MLPClassifier


class MyMlpClassifier:
    mlp = MLPClassifier(hidden_layer_sizes=100)

    def fitting(self, Xdata, ydata):
        self.mlp.fit(Xdata, ydata)

    def get_predict(self, Xdata):
        return self.mlp.predict(Xdata)
