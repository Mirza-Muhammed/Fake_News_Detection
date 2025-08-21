import re
import string

class TextCleaner:
    def __init__(self):
        pass

    def transform(self, texts):
        """Apply cleaning to a list of texts"""
        return [self._clean_text(text) for text in texts]

    def _clean_text(self, text):
        if not isinstance(text, str):
            return ""
        text = text.lower()
        text = re.sub(r"http\S+", "", text)  # remove URLs
        text = text.translate(str.maketrans("", "", string.punctuation))  # remove punctuation
        text = re.sub(r"\d+", "", text)  # remove numbers
        text = re.sub(r"\s+", " ", text).strip()  # remove extra spaces
        return text
