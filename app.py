from flask import Flask, render_template, request, jsonify
import os
from signature import match

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def upload_form():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file1' not in request.files or 'file2' not in request.files:
        return jsonify({'error': 'Please upload both signature files.'}), 400

    file1 = request.files['file1']
    file2 = request.files['file2']

    if file1.filename == '' or file2.filename == '':
        return jsonify({'error': 'Both files must have a name.'}), 400

    path1 = os.path.join(UPLOAD_FOLDER, file1.filename)
    path2 = os.path.join(UPLOAD_FOLDER, file2.filename)
    file1.save(path1)
    file2.save(path2)

    try:
        similarity = match(path1, path2)
        return jsonify({'similarity': round(similarity, 2)})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
