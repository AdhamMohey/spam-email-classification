import streamlit as st
import joblib
import re

# Load model and vectorizer
model = joblib.load("spam_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# Text cleaning function
def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    return text


st.title("Spam Email Classification")
st.write("Enter an email message below to check whether it is Spam or Not Spam.")

user_input = st.text_area("Enter Email Text")

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        cleaned_text = clean_text(user_input)
        vectorized_text = vectorizer.transform([cleaned_text])
        
        prediction = model.predict(vectorized_text)[0]

        if prediction == 1:
            st.error("This email is SPAM.")
        else:
            st.success("This email is NOT Spam (Ham).")

        if hasattr(model, "predict_proba"):
            probability = model.predict_proba(vectorized_text)[0][1]
            st.write(f"Spam Probability: {probability:.2f}")
