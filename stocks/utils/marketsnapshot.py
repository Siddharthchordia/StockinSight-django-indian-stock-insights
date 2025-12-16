import yfinance as yf

def get_live_snapshot(ticker: str):
    stock = yf.Ticker(f"{ticker}.NS")  
    info = stock.info

    return {
        "price": info.get("currentPrice"),
        "market_cap": info.get("marketCap"),
        "pe": info.get("trailingPE"),
        "pb": info.get("priceToBook"),
        "high_52w": info.get("fiftyTwoWeekHigh"),
        "low_52w": info.get("fiftyTwoWeekLow"),
    }
