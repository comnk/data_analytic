import yfinance as yf
from csv import *
from datetime import date

data = yf.Ticker("FB")
end_date = date.today().strftime("%Y-%m-%d")
start_date = date.today().strftime("-%m-%d")
yearly = data.history(start=str(int(date.today().strftime("%Y")) - 1)+start_date, end=end_date)
print(yearly.head())
print(type(yearly))

yearly.to_csv('data.csv')