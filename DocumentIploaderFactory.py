import os
from PDFUploader import PDFUploader
from WordUploader import WordUploader
from HTMLUploader import HTMLUploader
from TXTUploader import TXTUploader


class DocumentUploaderFactory:

    _registry = {
        ".pdf":  PDFUploader,
        ".doc":  WordUploader,
        ".docx": WordUploader,
        ".html": HTMLUploader,
        ".htm":  HTMLUploader,
        ".txt":  TXTUploader,
    }

    @classmethod
    def create_uploader(cls, file_path: str):
        _, ext = os.path.splitext(file_path)
        ext = ext.lower()
        uploader_class = cls._registry.get(ext)
        if uploader_class is None:
            raise ValueError(f"Unsupported file type '{ext}'. Supported: {', '.join(cls._registry.keys())}")
        return uploader_class(file_path)