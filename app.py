from flask import Flask, jsonify
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import nltk

nltk.download('punkt')
nltk.download('stopwords')

app = Flask(__name__)

@app.route('/')
def word_frequency():
    text = "Hello world! This is a test. Hello again."
    stop_words = set(stopwords.words('english'))

    word_tokens = word_tokenize(text)
    filtered_sentence = [w for w in word_tokens if not w in stop_words]

    word_freq = Counter(filtered_sentence)
    
    return jsonify(dict(word_freq))

if __name__ == '__main__':
    app.run(port=80, debug=False)
