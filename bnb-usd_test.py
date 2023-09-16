import pandas as pd
import statistics as st

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

df = pd.read_csv('BNB-USD.csv')
df = df[['Date', 'Close']]
df['change'] = df['Close'].pct_change()
df['ma'] = df['Close'].rolling(20).mean()
df['SD'] = df['Close'].rolling(20).std()*20

print(df)