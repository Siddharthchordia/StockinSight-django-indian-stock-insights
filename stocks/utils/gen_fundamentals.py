from decimal import Decimal
from stocks.models import (
    Company,
    FinancialValue,
    Metric,
    CompanyFundamental
)


def safe_div(a, b):
    if a is None or b in (None, 0):
        return None
    return (Decimal(a) / Decimal(b)) * 100


def get_latest_value(company, metric_code):
    try:
        metric = Metric.objects.get(code=metric_code.upper())
    except Metric.DoesNotExist:
        return None

    fv = (
        FinancialValue.objects
        .filter(company=company, metric=metric)
        .select_related("time_period")
        .order_by("-time_period__year", "-time_period__quarter")
        .first()
    )
    return fv.value if fv else None


def generate_company_fundamentals(company):

    revenue = get_latest_value(company, "SALES")
    net_profit = get_latest_value(company, "NET_PROFIT")
    operating_profit = get_latest_value(company, "OPERATING_PROFIT")

    equity_share_capital = get_latest_value(company, "EQUITY_SHARE_CAPITAL")
    reserves = get_latest_value(company, "RESERVES")
    total_debt = get_latest_value(company, "BORROWINGS")

    total_equity = (
        (equity_share_capital or 0) +
        (reserves or 0)
        if equity_share_capital or reserves else None
    )

    capital_employed = (
        (total_equity or 0) +
        (total_debt or 0)
        if total_equity or total_debt else None
    )

    operating_margin = safe_div(operating_profit, revenue)
    net_margin = safe_div(net_profit, revenue)
    roe = safe_div(net_profit, total_equity)
    roce = safe_div(operating_profit, capital_employed)
    debt_to_equity = safe_div(total_debt, total_equity)

    CompanyFundamental.objects.update_or_create(
        company=company,
        defaults={
            "revenue": revenue,
            "operating_margin": operating_margin,
            "net_margin": net_margin,
            "roe": roe,
            "roce": roce,
            "debt_to_equity": debt_to_equity,
        }
    )


def generate_all_company_fundamentals():
    for company in Company.objects.filter(is_active=True):
        generate_company_fundamentals(company)
