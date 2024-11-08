import pandas as pd
import yfinance as yf
import talib

# Mengambil data dari Yahoo Finance
data = yf.download(
    "BTC-USD",
    start='2020-01-01',
    end='2022-01-01'
)

# Mengonversi kolom ke numpy array 1D
open_prices = data['Open'].to_numpy().flatten()
high_prices = data['High'].to_numpy().flatten()
low_prices = data['Low'].to_numpy().flatten()
close_prices = data['Close'].to_numpy().flatten()

# Menggunakan fungsi CDLHAMMER dari TA-Lib
hammer = talib.CDLHAMMER(open_prices, high_prices, low_prices, close_prices)
hanging_man = talib.CDLHANGINGMAN(open_prices, high_prices, low_prices, close_prices)

buys = (hammer==100)
sells = (hanging_man == -100)

# Membuat DataFrame dari hasil sinyal
hammer_signal = pd.DataFrame({
    'Date': data.index,
    'Hammer': hammer
})

hangingman_signal = pd.DataFrame({
    'Date': data.index,
    'Hanging Man': hanging_man
})

buys_signal = pd.DataFrame({
    'Date': data.index,
    'Buys': buys
})

# Memfilter hanya tanggal di mana sinyal Hammer terdeteksi (nilai 100)
hammer_dates = hammer_signal[hammer_signal['Hammer'] == 100]
hangingman_dates = hangingman_signal[hangingman_signal['Hanging Man'] == -100]
buys_dates = buys_signal[buys_signal['Buys']]

# Menampilkan hasil
print(hammer_dates)
print(hangingman_dates)

print(buys_dates)