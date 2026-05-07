Student Name: Mais Arafeh 
Student ID: 221154

================================================
Design Pattern Used: Factory Method Pattern
================================================


================================================
Project Structure
================================================
 
DocumentUploader.py         -> Abstract base class (Abstract Product)
PDFUploader.py              -> Handles PDF files (Concrete Product)
WordUploader.py             -> Handles .doc / .docx files (Concrete Product)
HTMLUploader.py             -> Handles .html / .htm files (Concrete Product)
TXTUploader.py              -> Handles .txt files (Concrete Product)
DocumentUploaderFactory.py  -> Decides which uploader to use (Factory)
main.py                     -> Flask REST API — entry point


================================================
How to Run
================================================
 
1. Install dependencies:
   pip install flask werkzeug
 
2. Start the server:
   python main.py
 
3. Server runs at:
   http://127.0.0.1:5000

================================================

Method   : POST
URL      : http://127.0.0.1:5000/upload
Body     : form-data
Key      : file   (type: File)
Value    : Select any PDF / Word / HTML / TXT file

Expected response (success):
{
  "success": true,
  "file": "sample.pdf",
  "type": "PDFUploader",
  "preview": "..."
}


================================================
Other API Endpoints
================================================

GET  /supported-types  -> List all supported file types
POST /upload           -> Upload a document file    

================================================
Supported File Types
================================================
 
.pdf          -> PDFUploader
.doc / .docx  -> WordUploader
.html / .htm  -> HTMLUploader
.txt          -> TXTUploader
