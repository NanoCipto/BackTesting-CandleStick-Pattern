import matplotlib.pyplot as plt
import yfinance as yf
import mplfinance as mpf
import datetime as dt

# Mengambil data menggunakan yfinance
start = dt.datetime(2021, 1, 1)
end = dt.datetime.now()

# Mengambil data TSLA dari Yahoo Finance
data = yf.download('TSLA', start=start, end=end)

# Mengatasi masalah nilai NaN dengan mengisi menggunakan metode forward fill
data = data.fillna(method='ffill')

# Konversi tipe data ke float
data = data.astype(float)

# Plot harga penutupan (Close)
plt.plot(data['Close'])
plt.title('Tesla (TSLA) Stock Price')
plt.xlabel('Date')
plt.ylabel('Close Price')
# plt.show()

# Membuat grafik candlestick menggunakan mplfinance
mpf.plot(data, type='candle', style='charles', title='TSLA Candlestick Chart', volume=True)
