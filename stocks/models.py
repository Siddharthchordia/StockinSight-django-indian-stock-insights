from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


class Company(models.Model):

    EXCHANGE_CHOICES = (
        ("nse", "NSE"),
        ("bse", "BSE"),
    )

    name = models.CharField(_("Name"), max_length=50, unique=True)
    ticker = models.CharField(_("Ticker"), max_length=30, unique=True)
    exchange = models.CharField(_("Exchange"), max_length=3, choices=EXCHANGE_CHOICES)
    sector = models.CharField(_("Sector"), max_length=50)
    listing_date = models.DateField(_("Listing Date"))
    is_active = models.BooleanField(_("Active?"), default=True)

    class Meta:
        verbose_name = _("Company")
        verbose_name_plural = _("Companies")
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.ticker})"


class TimePeriod(models.Model):

    PERIOD_TYPE_CHOICES = (
        ("annual", "Annual"),
        ("quarterly", "Quarterly"),
    )

    year = models.SmallIntegerField(_("Year"))
    quarter = models.SmallIntegerField(_("Quarter"), null=True, blank=True)
    period_type = models.CharField(
        _("Period Type"),
        max_length=10,
        choices=PERIOD_TYPE_CHOICES,
    )

    class Meta:
        verbose_name = _("Time Period")
        verbose_name_plural = _("Time Periods")
        unique_together = ("year", "quarter", "period_type")
        ordering = ["-year", "-quarter"]

    def __str__(self):
        if self.period_type == "quarterly":
            return f"FY{self.year} Q{self.quarter}"
        return f"FY{self.year} {self.period_type.upper()}"

class MetricCategory(models.Model):

    CATEGORY_CHOICES = (
        ("PNL", "Profit & Loss"),
        ("BS", "Balance Sheet"),
        ("CF", "Cash Flow"),
    )

    code = models.CharField(
        _("Category Code"),
        max_length=10,
        choices=CATEGORY_CHOICES,
        unique=True
    )

    class Meta:
        verbose_name = _("Metric Category")
        verbose_name_plural = _("Metric Categories")

    def __str__(self):
        return dict(self.CATEGORY_CHOICES).get(self.code, self.code)

class Metric(models.Model):

    

    code = models.CharField(_("Metric Code"), max_length=50, unique=True)
    name = models.CharField(_("Name"), max_length=100)
    category = models.ForeignKey(
        MetricCategory,
        verbose_name=_("Category"),
        on_delete=models.PROTECT,
        related_name="metrics"
    )
    formula = models.TextField(_("Formula"), null=True, blank=True)

    class Meta:
        verbose_name = _("Metric")
        verbose_name_plural = _("Metrics")
        ordering = ["category", "name"]

    def __str__(self):
        return self.name


class FinancialValue(models.Model):

    company = models.ForeignKey(
        Company,
        verbose_name=_("Company"),
        on_delete=models.CASCADE,
        related_name="financials",
    )
    metric = models.ForeignKey(
        Metric,
        verbose_name=_("Metric"),
        on_delete=models.CASCADE,
        related_name="values",
    )
    time_period = models.ForeignKey(
        TimePeriod,
        verbose_name=_("Time Period"),
        on_delete=models.CASCADE,
        related_name="values",
    )
    value = models.DecimalField(
        _("Value"),
        max_digits=20,
        decimal_places=4,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = _("Financial Value")
        verbose_name_plural = _("Financial Values")
        unique_together = ("company", "metric", "time_period")
        indexes = [
            models.Index(fields=["company", "metric", "time_period"]),
        ]

    def __str__(self):
        return f"{self.company} | {self.metric} | {self.time_period}"

    def get_absolute_url(self):
        return reverse("financialvalue_detail", kwargs={"pk": self.pk})


class CompanyFundamental(models.Model):

    company = models.OneToOneField(
        Company,
        on_delete=models.CASCADE,
        related_name="fundamentals"
    )

    # Latest annual numbers
    revenue = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)

    # Margins (%)
    operating_margin = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    net_margin = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    # Returns (%)
    roce = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    roe = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    # Leverage
    debt_to_equity = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    # Growth (% CAGR)
    sales_cagr_5y = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    profit_cagr_5y = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Company Fundamental")
        verbose_name_plural = _("Company Fundamentals")

    def __str__(self):
        return f"{self.company.name} Fundamentals"

class CompanyMarketSnapshot(models.Model):

    company = models.OneToOneField(
        Company,
        on_delete=models.CASCADE,
        related_name="market"
    )

    price = models.DecimalField(max_digits=10, decimal_places=2)
    market_cap = models.DecimalField(max_digits=20, decimal_places=2)

    # Price-derived ratios
    pe = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    pb = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    dividend_yield = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.company.name} Market Snapshot"
