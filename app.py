from flask import Flask, render_template
import nltk
from nltk.tokenize import sent_tokenize

app = Flask(__name__)

@app.route('/')
def home():
    sample_paragraph = "I am Mr. Jones. What do you think... This is the first sentence. Here's another sentence. And yet one more sentence. NLTK is great for natural language processing!"
    sentences = sent_tokenize(sample_paragraph)

    return render_template('index.html', sentences=sentences)

if __name__ == '__main__':
    # Download the Punkt tokenizer. This is required by sent_tokenize.
    nltk.download('punkt')

    app.run(debug=True)
