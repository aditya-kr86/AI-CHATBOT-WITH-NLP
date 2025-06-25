NAME: ADITYA KUMAR    
INTERN ID: CT04DF1784     
DOMAIN: PYTHON PROGRAMMING      
DURATION: 30th May 2025 TO 30th June 2025      
MENTOR NAME: NEELA SANTHOSH KUMAR  
---
# AI Chatbot with NLP

A simple yet powerful NLP-powered chatbot built using Python, Streamlit, and scikit-learn. This chatbot can understand user input, classify intent, and generate appropriate responses, while also logging all conversations to a local SQLite database.

## Features

- **Streamlit UI:** Intuitive web-based chat interface.
- **NLP Intent Detection:** Uses TF-IDF and Logistic Regression for classifying user intent.
- **Customizable Intents:** Easily add or modify intents and responses via a JSON file.
- **Persistent Chat Logging:** All conversations are saved to an SQLite database for review or analysis.
- **Lightweight & Extensible:** Easy to modify for your own use-cases.

## Demo
![Screenshot 2025-06-25 061142](https://github.com/user-attachments/assets/5490a879-1791-46d1-bf81-35b01d8678bc)

![Chatbot Demo](https://raw.githubusercontent.com/aditya-kr86/AI-CHATBOT-WITH-NLP/main/demo.gif) <!-- Replace with actual demo GIF if available -->

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/aditya-kr86/AI-CHATBOT-WITH-NLP.git
cd AI-CHATBOT-WITH-NLP
```

### 2. Install Dependencies

Ensure you have Python 3.7+ installed. Then run:

```bash
pip install -r requirements.txt
```

**Required Python packages:**
- `streamlit`
- `scikit-learn`
- `nltk`
- `numpy`
- `sqlite3` (standard library)

### 3. Download NLTK Data

The app will attempt to download required NLTK corpora (`punkt` and `wordnet`) automatically. If you encounter issues, run:

```python
import nltk
nltk.download('punkt')
nltk.download('wordnet')
```

### 4. Run the Chatbot

```bash
streamlit run chatbot_app.py
```

Visit the provided localhost URL in your browser to start chatting!

---

## File Structure

- `chatbot_app.py` — Streamlit app that runs the chatbot UI and manages chat state.
- `model_utils.py` — Handles intent classification, model training, and bot response logic.
- `db_utils.py` — Manages SQLite database creation and logging of chat history.
- `intents.json` — (Required) Defines all chatbot intents, patterns, and responses. *(Add your custom intents here!)*
- `chat_log.db` — SQLite database file storing chat history (auto-created on first run).

---

## How It Works

1. **Model Training:** On startup, the app loads and trains a Logistic Regression model on the example sentences ("patterns") for each intent using TF-IDF features.
2. **User Input:** When you type a message, the app predicts the most likely intent and selects a random response from the corresponding intent.
3. **Logging:** Every question and answer (plus the detected intent) is logged to a local SQLite database with a timestamp.

---

## Customization

- **Add/Modify Intents:** Edit the `intents.json` file to add new tags, patterns, or responses.
- **Change Model/Vectorizer:** Modify `model_utils.py` to use a different ML model or text processing pipeline.
- **UI Tweaks:** Edit `chatbot_app.py` to update the Streamlit interface per your needs.

---

## License

This project is open-source and available under the [MIT License](LICENSE).

---

*Made with ❤️ by [Aditya Kumar](https://adityakr.me)*

