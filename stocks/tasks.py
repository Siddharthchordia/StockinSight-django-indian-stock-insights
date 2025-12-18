from celery import shared_task
from django.db import transaction
from stocks.models import Company
from stocks.utils.marketsnapshot import get_live_snapshot, get_weekly_updates


@shared_task(bind=True, autoretry_for=(Exception,), retry_backoff=60, retry_kwargs={"max_retries": 3})
def daily_market_snapshot(self):
    for company in Company.objects.filter(is_active=True):
        with transaction.atomic():
            get_live_snapshot(company)


@shared_task(bind=True, autoretry_for=(Exception,), retry_backoff=300, retry_kwargs={"max_retries": 2})
def weekly_market_update(self):
    for company in Company.objects.filter(is_active=True):
        with transaction.atomic():
            get_weekly_updates(company)

