import os
from DocumentIploaderFactory import DocumentUploaderFactory
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)

# folder to save uploaded files temporarily
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

ALLOWED_EXTENSIONS = {".pdf", ".doc", ".docx", ".html", ".htm", ".txt"}


def allowed_file(filename: str) -> bool:
    _, ext = os.path.splitext(filename)
    return ext.lower() in ALLOWED_EXTENSIONS

@app.route("/upload", methods=["POST"])
def upload_document():
    if "file" not in request.files:
        return jsonify({"success": False, "message": "No file part in the request."}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"success": False, "message": "No file selected."}), 400

    if not allowed_file(file.filename):
        return jsonify({
            "success": False,
            "message": f"Unsupported file type. Allowed: {', '.join(ALLOWED_EXTENSIONS)}"
        }), 400

    # save file temporarily
    filename = secure_filename(file.filename)
    saved_path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(saved_path)

    try:
        uploader = DocumentUploaderFactory.create_uploader(saved_path)
        result = uploader.upload()
        return jsonify(result), 200 if result["success"] else 422
    except ValueError as e:
        return jsonify({"success": False, "message": str(e)}), 400
    finally:
        if os.path.exists(saved_path):
            os.remove(saved_path)


@app.route("/supported-types", methods=["GET"])
def supported_types():
    return jsonify({
        "supported_extensions": list(ALLOWED_EXTENSIONS)
    }), 200


if __name__ == "__main__":
    app.run(debug=True, port=5000)