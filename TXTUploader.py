import os
from DocumentUploader import DocumentUploader


class TXTUploader(DocumentUploader):

    def validate(self) -> bool:
        return self.file_path.lower().endswith(".txt") and os.path.exists(self.file_path)

    def process(self) -> str:
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                return f.read().strip()
        except Exception:
            return f"[TXT] Reading plain text from '{self.file_name}'."