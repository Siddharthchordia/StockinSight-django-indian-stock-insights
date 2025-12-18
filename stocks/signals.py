from stocks.models import MetricCategory

def create_metric_categories(sender, **kwargs):
    for code, _ in MetricCategory.CATEGORY_CHOICES:
        MetricCategory.objects.get_or_create(code=code)
