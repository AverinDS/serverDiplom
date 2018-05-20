import pandas as pd
import numpy as np

class RollingHelper():
    def rolling_mean(self, y):
        y = y.ravel()
        dataframe = pd.DataFrame({'y' : y})
        dataframe['y'] = dataframe['y'].rolling(int(len(y)/4), win_type='triang').mean()
        for i in range(len(dataframe)):
            if np.isnan(dataframe['y'][i]):
                dataframe['y'][i] = y[i]
            else:
                break

        print(np.array(dataframe, dtype=int))
        return np.array(dataframe, dtype=int)
