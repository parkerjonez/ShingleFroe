# Import the necessary modules
# from nltk.tokenize import sent_tokenize
import nltk
from .language_detection_service import detect_language
from flask import current_app

def segment_text(transcript_id, text, language=None):
    """
    This function segments the input text into sentences.

    Parameters:
    transcript_id (str): The ID of the transcript
    text (str): The input text
    language (str, optional): The language of the input text. If not provided, language detection will be performed.

    Returns:
    dict: A dictionary containing the status of the operation, the original text, the segmented sentences, 
    the language, and the transcript ID.
    """

    # If language is not provided, perform language detection
    if not language:
        try:
            # Perform language detection
            language_detection = detect_language(text)
            language = language_detection['fasttext']['detected_language']

            # Get confidence threshold from configuration
            confidence_threshold = current_app.confidence_threshold

            # Check the confidence of the detected language
            if language_detection['fasttext']['confidence'] < confidence_threshold:
                return {"status": "error", "message": "Confidence in language detection is too low. Please specify a language."}
        except Exception as e:
            return {"status": "error", "message": f"Language detection failed: {str(e)}"}

    # Get the supported languages from the application config
    supported_languages = current_app.nltk_supported_languages

    # Check if the detected language is supported
    if language not in supported_languages:
        return {"status": "error", "message": f"Language {language} is not supported."}

    try:
        # Download NLTK 'punkt' resource for sentence tokenization
        nltk.download('punkt')
    except Exception as e:
        return {"status": "error", "message": f"Downloading 'punkt' failed: {str(e)}"}

    try:
        # Perform text segmentation into sentences
        sent_detector = nltk.data.load('tokenizers/punkt/' + supported_languages[language] + '.pickle')
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
