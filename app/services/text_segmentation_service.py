# Import the necessary modules
import nltk
from .language_detection_service import detect_language
from flask import current_app

def segment_text(transcript_id, text, language=None):
    """
    This function segments the input text into sentences.
    """

    # If language is not provided, perform language detection
    if not language:
        try:
            language_detection = detect_language(text)
            language = language_detection['fasttext']['detected_language']
            if language_detection['fasttext']['confidence'] < 0.5:  # Adjust this threshold as needed
                return {"status": "error", "message": "Confidence in language detection is too low. Please specify a language."}
        except Exception as e:
            return {"status": "error", "message": f"Language detection failed: {str(e)}"}

    # Get the supported languages from the application config
    supported_languages = current_app.nltk_supported_languages

    # Check if the detected language is supported
    if language not in supported_languages.keys():
        return {"status": "error", "message": f"Language {language} is not supported."}

    # Download NLTK 'punkt' resource for sentence tokenization for the specific language
    try:
        nltk.download(f'punkt/{supported_languages[language]}')
    except Exception as e:
        return {"status": "error", "message": f"Downloading 'punkt/{supported_languages[language]}' failed: {str(e)}"}

    # Perform text segmentation into sentences
    try:
        sent_detector = nltk.data.load(f'tokenizers/punkt/{supported_languages[language]}.pickle')
        segments = sent_detector.tokenize(text.strip())
    except Exception as e:
        return {"status": "error", "message": f"Text segmentation failed: {str(e)}"}

    return {
        "status": "success",
        "original_text": text,
        "segments": segments,
        "language": language,
        "transcript_id": transcript_id
    }
