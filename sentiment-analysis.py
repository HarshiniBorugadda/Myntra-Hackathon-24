import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
nltk.download('vader_lexicon')
df = pd.read_csv('blog_data.csv')
sid = SentimentIntensityAnalyzer()
df['sentiment'] = df['Content'].apply(lambda content: sid.polarity_scores(content)['compound'])
df.to_csv('sentiment_data.csv', index=False)
