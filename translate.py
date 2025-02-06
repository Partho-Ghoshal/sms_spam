from transformers import pipeline

# Initialize the translation pipeline
translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-xx")

def translate_text(text):
    languages = ['hi', 'mr', 'gu', 'ta', 'kn', 'te', 'bn', 'ml', 'pa', 'or']
    translations = {}
    
    for lang in languages:
        # Translate to the respective language
        model_name = f"Helsinki-NLP/opus-mt-en-{lang}"
        translator = pipeline("translation", model=model_name)
        translation = translator(text, max_length=512)
        translations[lang] = translation[0]['translation_text']
        
    return translations
