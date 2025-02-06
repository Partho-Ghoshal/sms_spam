import os
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'txt', 'docx', 'mp4', 'mov'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def handle_file_upload(file):
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join("uploads", filename))
        return jsonify({"message": "File uploaded successfully", "filename": filename}), 200
    else:
        return jsonify({"error": "File type not allowed"}), 400
