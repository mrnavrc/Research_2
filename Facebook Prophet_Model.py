import pandas as pd
from fbprophet import Prophet
import matplotlib.pyplot as plt

import time
start_time = time.time()

df = pd.read_csv("DATASET.csv")
df.Date = pd.to_datetime(df.Date, format="%d/%m/%y")
df.Transakce = df['Demand'].astype(float)
df = df.sort_index()
df.rename(columns = {"Date":"ds","Demand":"y"}, inplace = True)
y = df

y_to_train = y.iloc[:(len(y)-365)]
y_to_test = y.iloc[(len(y)-365):]

m = Prophet()
m.fit(y_to_train)
future = m.make_future_dataframe(periods=365)
forecast = m.predict(future)

plt.plot(forecast["yhat"].iloc[(len(y)-365):], label="Pred", color="black", zorder=1)
plt.plot(y_to_test["y"], label="True", color="lightgray", zorder=0)
plt.legend(loc="upper right")
plt.xlabel('Days', fontsize=10)
plt.ylabel('Demand', fontsize=10)
#fig1 = m.plot(forecast)
#fig2 = m.plot_components(forecast)

import numpy as np
Y_true = y_to_test["y"]
Y_pred = forecast["yhat"].iloc[(len(y)-365):]

from sklearn.metrics import mean_squared_error,mean_absolute_error
MSE = mean_squared_error(Y_true,Y_pred) 
MAE = mean_absolute_error(Y_true,Y_pred)

print(MSE)
print(MAE)
print("--- %s seconds ---" % (time.time() - start_time))