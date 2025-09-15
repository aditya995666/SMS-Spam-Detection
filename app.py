import streamlit as st
import pickle
import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Load saved models
tfidf = pickle.load(open("TFIDF.pkl", "rb"))
model = pickle.load(open("model_1.pkl", "rb"))



nltk.download("stopwords")
nltk.download("punkt")
nltk.download("punkt_tab")  
nltk.download("wordnet")

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

def transform_text(text):
    words = word_tokenize(text)  
    filtered_words = [
        lemmatizer.lemmatize(word.lower())
        for word in words
        if word.lower() not in stop_words and word.isalpha()
    ]
    return " ".join(filtered_words)  

# Streamlit UI
st.title(" Email/SMS Spam Classifier")

user_input = st.text_input("Enter the Message")

if st.button("Predict"):
    if user_input.strip() != "":
        cleaned_text = transform_text(user_input)
        
        vectorized = tfidf.transform([cleaned_text])
        prediction = model.predict(vectorized)[0]

        if prediction == 1:
            st.error(" This is a Spam message!")
        else:
            st.success(" This is NOT a Spam message.")
    else:
        st.warning(" Please enter a message first.")
