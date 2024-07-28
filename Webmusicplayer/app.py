from flask import Flask, request, send_from_directory, jsonify, render_template_string
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'kiwi'

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Serve the HTML file directly
@app.route('/')
def index():
    return render_template_string(open('index.html').read())

# Handle file uploads
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        file.save(os.path.join(UPLOAD_FOLDER, file.filename))
        return 'File uploaded successfully'

# Serve uploaded files
@app.route('/kiwi/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

# Get the list of uploaded files
@app.route('/files')
def list_files():
    files = os.listdir(UPLOAD_FOLDER)
    return jsonify(files)

if __name__ == '__main__':
    app.run(debug=True)
