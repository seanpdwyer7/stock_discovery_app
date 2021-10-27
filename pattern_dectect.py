import talib
import yfinance as yf
from datetime import date, timedelta

today = date.today()
year_ago = today-timedelta(days=365)

data = yf.download("SPY", start=year_ago, end=today)

morning_star = talib.CDLMORNINGSTAR(data['Open'], data['High'], data['Low'], data['Close'])

engulfing = talib.CDLENGULFING(data['Open'], data['High'], data['Low'], data['Close'])

data['Morning Star'] = morning_star
data['Engulfing'] = engulfing

engulfing_days = data[data['Engulfing'] != 0]

print(engulfing_days)