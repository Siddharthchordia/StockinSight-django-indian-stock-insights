from stocks.models import Company
from stocks.utils.marketsnapshot import get_live_snapshot
def regular_job():
    for company in Company.objects.filter(is_active=True):
        get_live_snapshot(company)