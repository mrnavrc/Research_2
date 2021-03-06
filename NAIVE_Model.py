import pandas as pd
import warnings
warnings.filterwarnings("ignore")
import matplotlib.pyplot as plt
import numpy as np
import time
start_time = time.time()
df = pd.read_csv("DATASET.csv")
df.set_index("Date", inplace=True)
df.index = pd.to_datetime(df.index, format="%d/%m/%y")
df.Demand = df['Demand'].astype(float)
y = df


y_forecast = y["2018-08-23":"2019-08-22"]
#y_forecast = y["2018-03-01":"2019-02-28"]
y_to_test = y.iloc[(len(y)-365):]
y_forecast = np.array(y_forecast)
y_to_test = np.array(y_to_test)

plt.plot(y_forecast, label="Pred", color="black", zorder=1)
plt.plot(y_to_test, label="True", color="lightgray", zorder=0)
plt.legend(loc="upper right")
plt.xlabel('Days', fontsize=10)
plt.ylabel('Demand', fontsize=10)


Y_true = y_to_test
Y_pred = y_forecast

from sklearn.metrics import mean_squared_error,mean_absolute_error
MSE = mean_squared_error(Y_true,Y_pred) 
MAE = mean_absolute_error(Y_true,Y_pred)

print(MSE)
print(MAE)
print("--- %s seconds ---" % (time.time() - start_time))