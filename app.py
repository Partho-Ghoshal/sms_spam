from flask import Flask, request, jsonify
from upload import handle_file_upload
from transcribe import transcribe_video
from translate import translate_text
from db import save_to_db, get_blog_metadata
from analytics import track_blog_view

app = Flask(__name__)

# Route to upload text or video
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('file')
    content_type = request.form.get('content_type')  # 'text' or 'video'
    
    if content_type == 'text':
        return handle_file_upload(file)
    elif content_type == 'video':
        transcription = transcribe_video(file)
        return jsonify({"transcription": transcription})
    else:
        return jsonify({"error": "Invalid content type"}), 400

# Route for translation and publishing the blog
@app.route('/publish_blog', methods=['POST'])
def publish_blog():
    blog_data = request.json
    original_text = blog_data.get('original_text')
    
    translations = translate_text(original_text)
    
    # Save blog and translations to DB
    blog_id = save_to_db(original_text, translations)
    
    return jsonify({
        "message": "Blog Published",
        "blog_id": blog_id,
        "translations": translations
    })

# Route for fetching blog metadata (views, engagement)
@app.route('/blog_metadata/<blog_id>', methods=['GET'])
def blog_metadata(blog_id):
    metadata = get_blog_metadata(blog_id)
    return jsonify(metadata)

# Route for tracking blog view (analytics)
@app.route('/track_view/<blog_id>', methods=['GET'])
def track_view(blog_id):
    track_blog_view(blog_id)
    return jsonify({"message": "View tracked"})

if __name__ == '__main__':
    app.run(debug=True)
