import pandas as pd

data = pd.read_csv('Fake.csv')
new_data = data['text'].head(10).to_csv('../fake_news.csv')
