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

    def double_exponential_smoothing(self, series, alpha, beta):
        result = [series[0]]
        for n in range(1, len(series) + 1):
            if n == 1:
                level, trend = series[0], series[1] - series[0]
            if n >= len(series):  # прогнозируем
                value = result[-1]
            else:
                value = series[n]
            last_level, level = level, alpha * value + (1 - alpha) * (level + trend)
            trend = beta * (level - last_level) + (1 - beta) * trend
            result.append(level + trend)
        return result
