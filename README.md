# 😊 NLP-Based Emotion Classification Using Machine Learning

A machine learning project that classifies text into one of six emotions:

**Sadness · Anger · Love · Surprise · Fear · Joy**

The project uses Natural Language Processing (NLP), text preprocessing, Bag-of-Words feature extraction, and Logistic Regression. A Streamlit web application is provided for real-time emotion prediction.

## 🚀 Live Demo

**Try the deployed application:**

https://nlp-based-emotion-classification-k4wptrntjunappzzpkgg5am.streamlit.app/

Enter any sentence and the application predicts its emotion.

### Example

```text
I can't believe how amazing this surprise gift was
```

**Prediction:** Surprise

```text
I feel so heartbroken since he left
```

**Prediction:** Sadness

---

## 📌 Emotions Classified

| Label | Emotion  |
| ----- | -------- |
| 0     | Sadness  |
| 1     | Anger    |
| 2     | Love     |
| 3     | Surprise |
| 4     | Fear     |
| 5     | Joy      |

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* NLTK
* Scikit-learn
* Joblib
* Streamlit
* Matplotlib
* Seaborn
* Git & GitHub

---

## 📂 Project Structure

```text
NLP-Based-Emotion-Classification/
│
├── app.py
├── Sentiment_Analysis.ipynb
├── train.txt
├── bow_vectorizer.pkl
├── emotion_model.pkl
├── emotion_numbers.pkl
├── tfidf_vectorizer.pkl
├── requirements.txt
└── README.md
```

### File Description

* `app.py` — Streamlit application for real-time predictions
* `Sentiment_Analysis.ipynb` — Complete data preprocessing, training, evaluation, and model comparison
* `train.txt` — Emotion classification dataset in `text;emotion` format
* `bow_vectorizer.pkl` — Saved CountVectorizer used by the deployed model
* `emotion_model.pkl` — Saved Logistic Regression model
* `emotion_numbers.pkl` — Emotion-to-number mapping
* `tfidf_vectorizer.pkl` — TF-IDF vectorizer from an alternate experiment
* `requirements.txt` — Python dependencies
* `README.md` — Project documentation

---

## 🔄 How the Project Works

### 1. Data Loading

The dataset is loaded from `train.txt`.

Each row contains:

```text
text;emotion
```

Example:

```text
i didnt feel humiliated;sadness
im grabbing a minute to post i feel greedy wrong;anger
```

### 2. Data Preprocessing

The text is cleaned using NLP preprocessing techniques such as:

* Lowercasing
* Punctuation removal
* Digit removal
* Non-ASCII character removal
* Tokenization
* Stopword removal during training

### 3. Duplicate Removal

Duplicate and near-duplicate sentences are removed to reduce data leakage and improve the reliability of model evaluation.

### 4. Feature Extraction

Two text representation approaches were experimented with:

* CountVectorizer / Bag-of-Words
* TfidfVectorizer

The deployed application uses **CountVectorizer (Bag-of-Words)**.

### 5. Model Training

Multiple machine learning models were compared.

| Model                                  | Approx. Accuracy |
| -------------------------------------- | ---------------: |
| Naive Bayes + Bag-of-Words             |             ~88% |
| Naive Bayes + TF-IDF                   |             ~89% |
| **Logistic Regression + Bag-of-Words** |         **~95%** |

**Logistic Regression with Bag-of-Words performed best among the tested models and is used in the deployed application.**

### 6. Prediction

When a user enters a sentence:

```text
I am extremely happy today
```

the application:

```text
Input Text
    ↓
Text Cleaning
    ↓
CountVectorizer
    ↓
Logistic Regression
    ↓
Emotion Prediction
```

The predicted emotion is displayed in the Streamlit application.

---

## 📊 Model Evaluation

The model was evaluated using:

* Confusion Matrix
* Accuracy
* Precision
* Recall
* F1-score

The confusion matrix helps identify which emotions are correctly classified and which emotions are commonly confused with each other.

Emotion classification is naturally more difficult for sentences with ambiguous or overlapping emotional meaning.

For example, expressions of **love and joy** can sometimes share similar words, while **sadness, anger, and fear** can also overlap depending on the context.

---

## 🧠 Why Logistic Regression?

Logistic Regression works well for high-dimensional sparse text features such as Bag-of-Words.

Advantages include:

* Simple and efficient
* Works well with sparse text data
* Fast training and prediction
* Easy to evaluate
* Performs well for multi-class text classification

---

## 💻 Installation

Clone the repository:

```bash
git clone https://github.com/tanishqkatiyar-sys/NLP-Based-Emotion-Classification.git
```

Move into the project directory:

```bash
cd NLP-Based-Emotion-Classification
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application Locally

Run:

```bash
streamlit run app.py
```

The application will open in your browser.

Usually:

```text
http://localhost:8501
```

---

## 🔁 Retrain the Model

Open:

```text
Sentiment_Analysis.ipynb
```

Run the notebook cells in order.

The training process generates:

```text
bow_vectorizer.pkl
emotion_model.pkl
emotion_numbers.pkl
```

These files should come from the **same training run** because the model expects the exact feature representation produced by its corresponding vectorizer.

---

## 📦 Requirements

The project uses:

```text
streamlit
joblib
pandas
numpy
scikit-learn==1.6.1
```

The scikit-learn version is pinned because the saved machine learning model was created using scikit-learn 1.6.1.

---

## 🌐 Deployment

The application is deployed using **Streamlit Community Cloud**.

### Live Application

https://nlp-based-emotion-classification-k4wptrntjunappzzpkgg5am.streamlit.app/

### Source Code

https://github.com/tanishqkatiyar-sys/NLP-Based-Emotion-Classification

---

## ⚠️ Limitations

* Emotion classification depends heavily on the wording and context of the input
* Difficult or ambiguous sentences may be classified incorrectly
* Some emotions have overlapping linguistic patterns
* Model performance on manually created sentences may differ from performance on the original test dataset
* Bag-of-Words does not understand sentence meaning as deeply as modern transformer-based models
* The saved model must be used with its corresponding vectorizer

---

## 🔮 Future Improvements

Possible improvements include:

* Try TF-IDF with additional classifiers
* Hyperparameter tuning
* Use word and character n-grams
* Handle negation more effectively
* Experiment with Support Vector Machines
* Try transformer-based models such as BERT
* Add confidence scores to predictions
* Improve the Streamlit interface
* Evaluate on a completely unseen real-world dataset

---

## 👨‍💻 Author

**Tanishq Katiyar**

GitHub:

https://github.com/tanishqkatiyar-sys

---

## 📄 License

This project is available for educational and portfolio purposes.
