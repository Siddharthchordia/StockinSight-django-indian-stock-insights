from django.core.management.base import BaseCommand
from stocks.utils.gen_fundamentals import generate_all_company_fundamentals


class Command(BaseCommand):
    help = "Generate company fundamentals from financial values"

    def handle(self, *args, **options):
        generate_all_company_fundamentals()
        self.stdout.write(self.style.SUCCESS("Company fundamentals generated successfully"))
