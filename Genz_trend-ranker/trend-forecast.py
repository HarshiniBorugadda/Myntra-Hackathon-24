import pandas as pd
from fbprophet import Prophet
df = pd.read_csv('trend_data.csv')
df['ds'] = pd.to_datetime(df['date'])
df['y'] = df['trend_value']
model = Prophet()
model.fit(df)
future = model.make_future_dataframe(periods=365)
forecast = model.predict(future)
forecast[['ds', 'yhat']].to_csv('forecast.csv', index=False)
