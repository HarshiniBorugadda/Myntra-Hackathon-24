import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('forecast.csv')
plt.figure(figsize=(10,6))
sns.lineplot(data=df, x='ds', y='yhat', label='Forecasted Trend')
plt.title('Trend Forecasting')
plt.xlabel('Date')
plt.ylabel('Forecasted Trend Value')
plt.savefig('trend_forecast_visualization.png')
plt.show()
