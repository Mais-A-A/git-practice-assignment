from abc import ABC, abstractmethod
import os


class DocumentUploader(ABC):
    """Abstract base class for all document uploaders."""

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.file_name = os.path.basename(file_path)

    @abstractmethod
    def validate(self) -> bool:
        pass

    @abstractmethod
    def process(self) -> str:
        pass

    def upload(self) -> dict:
        if not self.validate():
            return {
                "success": False,
                "file": self.file_name,
                "type": self.__class__.__name__,
                "message": f"Validation failed for '{self.file_name}'"
            }

        content_preview = self.process()
        return {
            "success": True,
            "file": self.file_name,
            "type": self.__class__.__name__,
            "preview": content_preview[:200]
        }