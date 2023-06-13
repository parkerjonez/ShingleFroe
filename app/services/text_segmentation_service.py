# app/services/text_segmentation_service.py
from .language_detection_service import detect_language

def segment_text(fasttext_model, transcript_id, text, language=None):
    if not language:
        try:
            language_detection = detect_language(fasttext_model, text)
            language = language_detection['fasttext']['detected_language']
            if language_detection['fasttext']['confidence'] < 0.5:  # Adjust this threshold as needed
                return {"status": "error", "message": "Confidence in language detection is too low. Please specify a language."}
        except Exception as e:
            return {"status": "error", "message": f"Language detection failed: {str(e)}"}

    # Add your text segmentation logic here using the 'text' and 'language' variables
    segments = ["El candidato de Vox en la Comunidad Valenciana se aparta para facilitar un Gobierno con el Partido Popular.", "Hola"]  # Placeholder

    return {
        "status": "success",
        "original_text": text,
        "segments": segments,
        "language": language,
        "transcript_id": transcript_id
    }
