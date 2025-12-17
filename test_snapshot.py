
import os
import django
import sys

# Add project root to path
sys.path.append('/Users/siddharthchordia/Developer/ProjectScreener')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stock_tracker.settings')
django.setup()

from stocks.models import Company, CompanyMarketSnapshot
from stocks.utils.marketsnapshot import get_live_snapshot

def test_tatasteel():
    ticker = "TATASTEEL"
    # Ensure company exists
    company, created = Company.objects.get_or_create(
        ticker=ticker,
        defaults={
            "name": "Tata Steel Ltd",
            "exchange": "nse",
            "sector": "Steel"
        }
    )
    print(f"Company: {company}")
    
    get_live_snapshot(company)
    
    # Verify snapshot
    try:
        # Re-fetch to get related object
        company.refresh_from_db()
        snapshot = company.market
        print(f"Snapshot created! Price: {snapshot.price}, Market Cap: {snapshot.market_cap}")
    except Exception as e:
        print(f"No snapshot found: {e}")

if __name__ == "__main__":
    test_tatasteel()
