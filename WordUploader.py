import os
from DocumentUploader import DocumentUploader


class WordUploader(DocumentUploader):

    def validate(self) -> bool:
        return self.file_path.lower().endswith((".doc", ".docx")) and os.path.exists(self.file_path)

    def process(self) -> str:
        return f"[Word] Parsing paragraphs and tables from '{self.file_name}'."