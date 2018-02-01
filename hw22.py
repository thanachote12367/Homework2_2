from flask import Flask, jsonify, request
from datetime import datetime, date

app = Flask(__name__)

@app.route('/files', methods=['GET', 'POST'])
def files():
    if request.method == 'POST':
        try:
            if 'file' not in request.files:
                print('No file part')
                return 'No file part'
            file = request.files['file']
            if file.filename == '':
                print('No selected file')
                return 'No selected file'
            return jsonify({ 'code': 200, 'desc': 'upload success'})
            pass
        except Exception as e:
            return jsonify({ 'code': 404, 'desc': str(e)})


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug = True, port=5000)
