import os
from DocumentUploader import DocumentUploader


class PDFUploader(DocumentUploader):

    def validate(self) -> bool:
        return self.file_path.lower().endswith(".pdf") and os.path.exists(self.file_path)

    def process(self) -> str:
        return f"[PDF] Reading binary PDF structure of '{self.file_name}'."