import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import word_tokenize


# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')

# Preprocessing function


def preprocess_text(text):
    # Step 1: Lowercase the text
    text = text.lower()

    # Step 2: Remove special characters, numbers, and unwanted symbols
    text = re.sub(r'[^a-z\s]', '', text)

    # Step 3: Tokenization
    tokens = word_tokenize(text)

    # Step 4: Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]

    # Step 5: Lemmatization
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]

    return ' '.join(tokens)


# Example
sample_text = "The quick brown fox jumped over 2 lazy dogs! #amazing"
processed_text = preprocess_text(sample_text)
print(processed_text)
