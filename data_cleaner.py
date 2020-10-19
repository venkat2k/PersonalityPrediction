import re
import re, string
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer


stemmer = SnowballStemmer("english")

class TextCleaner:

    stemmer = SnowballStemmer("english")

    def clean_data(self, text):
        text = text.lower()
        text = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", text).split())
        text = re.sub(r'http\S+', '', text)
        chars = re.escape(string.punctuation)
        text = re.sub(r'['+chars+']', '', text)
        words = text.split()
        clean_text = ""
        for word in words:
            if not word.isdigit():
                stem_text = stemmer.stem(word)
                if len(stem_text) > 2:
                    clean_text += stemmer.stem(word) + " ";
        return clean_text