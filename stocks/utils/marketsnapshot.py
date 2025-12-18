import yfinance as yf
from stocks.models import Company, CompanyMarketSnapshot, CompanyHistory
from datetime import date
from decimal import Decimal

def get_live_snapshot(company: Company):
    try:
        stock = yf.Ticker(f"{company.ticker}.NS")
        df = stock.history(period="1d")
        if df.empty:
            return
        price = Decimal(df["Close"].iloc[-1])
        volume = int(df["Volume"].iloc[-1])
        CompanyMarketSnapshot.objects.update_or_create(
            company=company,
            defaults={
                "price": price,
            }
        )
        CompanyHistory.objects.update_or_create(
            company=company,
            date=date.today(),
            defaults={
                "closing_price": price,
                "volume": volume,
            }
        )
    except Exception as e:
        print(f"Failed for {company.ticker}: {e}")

def get_weekly_updates(company: Company):
    stock = yf.Ticker(f"{company.ticker}.NS")
    info = stock.info

    CompanyMarketSnapshot.objects.update_or_create(
        company=company,
        defaults={
            "market_cap": info.get("marketCap"),
            "pe": info.get("trailingPE"),
            "pb": info.get("priceToBook"),
            "high_52w": info.get("fiftyTwoWeekHigh"),
            "low_52w": info.get("fiftyTwoWeekLow"),
        }
    )
