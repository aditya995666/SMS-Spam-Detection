# About Dataset
# Context
The SMS Spam Collection is a set of SMS tagged messages that have been collected for SMS Spam research. It contains one set of SMS messages in English of 5,574 messages, tagged acording being ham (legitimate) or spam.

# Content
The files contain one message per line. Each line is composed by two columns: v1 contains the label (ham or spam) and v2 contains the raw text.

This corpus has been collected from free or free for research sources at the Internet:



# SMS Spam Detection Project - Technical PowerPoint Content 📊

# Slide 1: Project Title 🎯

Title: SMS Spam Detection using Machine Learning 🤖

Name: Aditya Verma 👨‍💻

Date: April 2025 📅

# Slide 2: Objective 🎯

Detect whether a given SMS is spam or not using ML techniques 🔍📨

Improve accuracy and reduce false spam predictions 📈❌

# Slide 3: Dataset Overview 📂

Source: UCI SMS Spam Collection Dataset 🌐

Total messages: 5572 ✉️

Spam: 747 🚫

Ham: 4825 ✅

Format: Two columns - Label and Message 🧾

# Slide 4: Data Preprocessing 🛠️

Converted text to lowercase 🔤

Removed punctuation and special characters ❗

Tokenized the text ✂️

Removed stopwords ❌📃

Applied stemming using PorterStemmer 🌱

# Slide 5: Feature Extraction 🔎

Used TF-IDF Vectorizer 📏

ngram_range = (1, 2) ➡️ Unigrams & Bigrams 📚

max_features = 5000 🔢

Transformed clean text into numerical vectors 🔣

# Slide 6: Model Selection 🤖

Models Tried:

Multinomial Naive Bayes 🧠

Logistic Regression 📊

Support Vector Machine (SVM) ⚙️

Evaluation: Accuracy, Precision, Recall, F1-Score 📈

# Slide 7: Model Evaluation 🧪

Best Model: Multinomial Naive Bayes 🥇

Train/Test Split: 80/20 📘📕

Accuracy: 99.7% ✅

Precision: 99% 🎯

# Slide 8: Confusion Matrix 🔢

True Positives (Spam correctly detected): High 🔍✅

True Negatives (Ham correctly detected): High 📩✅

False Positives (Ham as Spam): Low 🚫📩

False Negatives (Spam as Ham): Low ⚠️📤

# Slide 9: Libraries Used 🧰

pandas, numpy: Data handling 📊

sklearn: Modeling & metrics 🧠

nltk: NLP preprocessing 🧹

matplotlib, seaborn: Visualization 📈

# Slide 10: Conclusion ✅

Built spam detection model using NLP & ML 🧠📱

High performance with Naive Bayes and RandomForestClassification + TF-IDF 🌟





