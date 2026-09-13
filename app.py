import streamlit as st
import joblib
import string

# Load model and vectorizer
model = joblib.load("emotion_model.pkl")
bow_vectorizer = joblib.load("bow_vectorizer.pkl")
emotion_numbers = joblib.load("emotion_numbers.pkl")

# Reverse mapping
number_emotions = {
    value: key
    for key, value in emotion_numbers.items()
}

def clean_text(text):
    text = text.lower()
    for punc in string.punctuation:
        text = text.replace(punc, '')
    text = ''.join(c for c in text if not c.isdigit())
    text = ''.join(c for c in text if c.isascii())
    return text


# Page title
st.title("😊 Emotion Detection App")

st.write("Enter a sentence and the model will predict your emotion.")


# User input
text = st.text_area(
    "Enter your text:",
    placeholder="Example: I am very happy today!"
)


# Button
if st.button("Predict Emotion"):

    if text.strip() == "":
        st.warning("Please enter some text.")

    else:

        # Clean, then convert text into bag-of-words
        cleaned = clean_text(text)
        text_bow = bow_vectorizer.transform([cleaned])

        # Predict
        prediction = model.predict(text_bow)[0]

        # Convert number to emotion
        emotion = number_emotions[prediction]

        # Display result
        st.success(f"Predicted Emotion: {emotion}")