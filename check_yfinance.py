
import yfinance as yf

def check_ticker(ticker):
    print(f"Checking {ticker}...")
    stock = yf.Ticker(ticker)
    info = stock.info
    print(f"currentPrice (info): {info.get('currentPrice')}")
    
    print("--- fast_info ---")
    try:
        fast_info = stock.fast_info
        print(f"last_price: {fast_info.last_price}")
        print(f"market_cap: {fast_info.market_cap}")
    except Exception as e:
        print(f"fast_info failed: {e}")

if __name__ == "__main__":
    check_ticker("TATASTEEL.NS")
