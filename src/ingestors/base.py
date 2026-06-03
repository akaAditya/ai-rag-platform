import os
from abc import ABC, abstractmethod

# BASE CLASS: Validation and Rules (Abstraction)

class BaseIngestor(ABC):
    def __init__(self, file_path):
        self.file_path = file_path
    
    def validate_path(self):
        """Robust Path Validtion for the Ingestion Enginer"""
        if not os.path.exists(self.file_path): # ye line check karti hai ki jo file path provide kiya gaya hai usme file exist karti hai ya nahi
            raise FileNotFoundError(f"[ERROR] Source file not found at: {self.file_path}")
        print(f"[VALIDATION SUCCESS] file found: {os.path.basename(self.file_path)}")

    @abstractmethod
    def extract_data(self):
        """Force every child ingestor to implement its own parsing logic"""
        pass