import csv
from src.ingestors.base import BaseIngestor
from src.utils.decorators import time_it
# CHILD CLASSES: Polymorphic Parsers

class CSVIngestor(BaseIngestor):
    @time_it
    def extract_data(self):
        self.validate_path()
        print(f"[PARSING] Extracting structured rows from CSV...")
        cleaned_data = []

        with open(self.file_path, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                # Basic cleaning: stripping spaces from keys/values
                cleaned_row = {k.strip(): v.strip() for k, v in row.items()}
                cleaned_data.append(cleaned_row)

        return cleaned_data