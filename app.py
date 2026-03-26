import streamlit as st
from langchain_community.chat_models import ChatOllama

st.set_page_config(page_title="Local AI Chatbot", layout="wide")
st.title("💬 Local AI Chatbot (Ollama + LangChain)")

# Use llama3 model (more stable)
llm = ChatOllama(model="llama3")

# Store messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# User input
user_input = st.text_input("Ask something:")

if st.button("Send") and user_input:
    st.session_state.messages.append(("You", user_input))

    response = llm.invoke(user_input)
    st.session_state.messages.append(("Bot", response.content))

# Display chat
for sender, msg in st.session_state.messages:
    if sender == "You":
        st.markdown(f"**🧑 You:** {msg}")
    else:
        st.markdown(f"**🤖 Bot:** {msg}")