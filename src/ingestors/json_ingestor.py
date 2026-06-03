import json
from src.ingestors.base import BaseIngestor
from src.utils.decorators import time_it

class JSONIngestor(BaseIngestor):
    @time_it
    def extract_data(self):
        self.validate_path()
        print(f"[PARSING] Extracting semi-structured objects from JSON...")
        
        with open(self.file_path, mode='r', encoding='utf-8') as file:
            raw_data = json.load(file)

        # Standardizing output to a list of dicts for RAG Chunking
        if isinstance(raw_data, list):
            return raw_data
        return [raw_data]