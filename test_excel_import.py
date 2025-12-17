import yfinance as yf


symbol = "INFY.NS"
stock = yf.Ticker(symbol)
info = stock.info

print(info)
print(info.get('industry'))
