from stocks.utils.marketsnapshot import get_live_snapshot
from django.core.management.base import BaseCommand
from stocks.models import Company

class Command(BaseCommand):
    def handle(self,*args, **options):
        company = Company.objects.get(ticker="SWIGGY")
        get_live_snapshot(company)

