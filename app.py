from flask import Flask, request, jsonify
import nltk
from nltk.tokenize import sent_tokenize

nltk.download('punkt')

app = Flask(__name__)

@app.route('/segment', methods=['POST'])
def segment_text():
    text = request.get_json().get('text', '')
    sentences = sent_tokenize(text)
    return jsonify(sentences)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
