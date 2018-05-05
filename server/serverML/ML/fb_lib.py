from fbprophet import Prophet
from pandas import DataFrame
import numpy as np


class FbLib:
    model = Prophet()

    def make_model(self):
        self.model = Prophet()

    def fit(self, X, Y):
        X = X.tolist()
        Y = Y.tolist()

        points = []

        for i, j in zip(X, Y):
            print("X=", i, "Y=", j)
            points.append([i[0], j[0]])


        df = DataFrame(data=points,columns=['ds','y'])
        print(df.head(5))
        self.model.fit(df)

    def predict(self, X):
        df = DataFrame(data=X,columns=['ds'])
        predict = self.model.predict(df)
        print (predict['yhat_lower'])

        return np.array(predict['yhat_lower'].tolist())


