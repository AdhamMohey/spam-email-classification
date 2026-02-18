# 📧 Spam Email Detection App

A Machine Learning web application that classifies emails as **Spam** or **Ham (Not Spam)** using Natural Language Processing and Logistic Regression.

---

## 🚀 Project Overview

This project builds a spam detection system using:

- 🧹 Text Cleaning (Regex + Preprocessing)
- 📊 TF-IDF Vectorization
- 🤖 Logistic Regression Model
- 🌐 Streamlit Web Application

The model predicts whether an email message is:

- ✅ Ham (Legitimate Email)
- ❌ Spam (Unwanted Email)

---

## 🧠 Machine Learning Pipeline

1. Text preprocessing
2. TF-IDF vectorization
3. Model training (Logistic Regression)
4. Model evaluation
5. Deployment using Streamlit

---

## 📂 Project Structure

```text
spam-email-classification/
│
├── app.py                    # Streamlit application
├── dataset.csv               # Email dataset
├── spam_model.pkl            # Trained ML model
├── tfidf_vectorizer.pkl      # TF-IDF vectorizer
├── training_notebook.ipynb   # Model training notebook
├── requirements.txt          # Dependencies
├── README.md                 # Project documentation
└── .gitignore                # Ignored files

