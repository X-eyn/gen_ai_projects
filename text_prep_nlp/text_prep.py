import nltk
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# # Download necessary NLTK data if not already done
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

# Reading from the file
file_path = r"C:\Users\Admin\Downloads\Python OOP\genai_intern_projects\text_prep_nlp\input.txt"  # Use raw string

with open(file_path, 'r', encoding='utf-8') as file:
    # Read the file content
    text = file.read()

    # Preprocess the text
    processed_text = preprocess_text(text)
    print(processed_text)
