import vectorbt as vbt
import pandas as pd
import yfinance as yf
import talib

help(talib.CDLHAMMER)

# # Mengambil data dari Yahoo Finance
# data = yf.download(
#     "BTC-USD",
#     start='2020-01-01',
#     end='2022-01-01'
# )

# # Mengonversi kolom ke numpy array 1D
# open_prices = data['Open'].to_numpy()
# high_prices = data['High'].to_numpy()
# low_prices = data['Low'].to_numpy()
# close_prices = data['Close'].to_numpy()

# # Menggunakan fungsi CDLHAMMER dan CDLHANGINGMAN dari TA-Lib
# hammer = talib.CDLHAMMER(open_prices, high_prices, low_prices, close_prices)
# hanging_man = talib.CDLHANGINGMAN(open_prices, high_prices, low_prices, close_prices)

# # Menentukan sinyal buy dan sell
# buys = (hammer == 100)
# sells = (hanging_man == -100)

# # Membuat DataFrame dari hasil sinyal
# signal_df = pd.DataFrame({
#     'Date': data.index,
#     'Hammer': hammer,
#     'Hanging Man': hanging_man,
#     'Buys': buys,
#     'Sells': sells
# })

# # Membuat portfolio dengan vectorbt
# pf = vbt.Portfolio.from_signals(data['Close'], buys, sells)

# # Menampilkan plot dan statistik
# # pf.stats() bisa ditampilkan jika Anda butuh informasi statistik
# pf.plot().show()

# # Menampilkan DataFrame dengan status buys dan sells untuk setiap hari
# print(signal_df[['Date', 'Buys', 'Sells', 'Hammer', 'Hanging Man']])