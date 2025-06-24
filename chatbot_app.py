import streamlit as st
from model_utils import train_bot_model, get_bot_response
from db_utils import init_db, log_chat
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load model and intents
model, data = train_bot_model()
init_db()

st.title("🧠 Smart NLP Chatbot")
st.write("Ask me anything!")

# Chat state
if "history" not in st.session_state:
    st.session_state.history = []

# Input box
user_input = st.text_input("You:", key="input")

if user_input:
    response, intent = get_bot_response(model, data, user_input)
    
    # Log and display
    st.session_state.history.append(("You", user_input))
    st.session_state.history.append(("Bot", response))
    log_chat(user_input, response, intent)

# Display history
for speaker, text in st.session_state.history:
    if speaker == "You":
        st.markdown(f"**🧑‍💻 You:** {text}")
    else:
        st.markdown(f"**🤖 Bot:** {text}")
