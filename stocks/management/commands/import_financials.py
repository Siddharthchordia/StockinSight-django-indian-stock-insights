from django.core.management.base import BaseCommand, CommandError
from stocks.utils.import_excel import import_data_sheet
import os


class Command(BaseCommand):
    help = "Import financial data from Excel Data Sheet and regenerate fundamentals"

    def add_arguments(self, parser):
        parser.add_argument(
            "file_path",
            type=str,
            help="Path to Excel file (e.g. data/SBI.xlsx)",
        )
        parser.add_argument(
            "company_ticker",
            type=str,
            help="Company ticker (e.g. SBIN)",
        )

    def handle(self, *args, **options):
        file_path = options["file_path"]
        company_ticker = options["company_ticker"].upper()

        if not os.path.exists(file_path):
            raise CommandError(f"File not found: {file_path}")

        self.stdout.write("Starting financial data import...")

        try:
            company = import_data_sheet(
                file_path=file_path,
                company_ticker=company_ticker,
            )
        except Exception as e:
            raise CommandError(str(e))

        self.stdout.write(
            self.style.SUCCESS(
                f"✔ Import completed successfully for {company.ticker}"
            )
        )
