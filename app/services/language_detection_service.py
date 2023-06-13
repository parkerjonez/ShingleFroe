# app/services/language_detection_service.py
from langdetect import detect_langs

def detect_language(fasttext_model, text):
    # Detect the language of the text with langdetect
    langdetect_languages = detect_langs(text)
    langdetect_most_likely_language = langdetect_languages[0]  # Get the most likely language

    # Detect the language of the text with FastText
    fasttext_prediction = fasttext_model.predict(text)[0][0]  # Get the predicted language
    fasttext_most_likely_language = fasttext_prediction.replace('__label__', '')  # Remove the '__label__' prefix

    return {
        "original_text": text,
        "langdetect": {
            "detected_language": langdetect_most_likely_language.lang,
            "confidence": langdetect_most_likely_language.prob
        },
        "fasttext": {
            "detected_language": fasttext_most_likely_language,
            "confidence": fasttext_model.predict(text)[1][0]
        }
    }
