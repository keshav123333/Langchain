import streamlit as st
import uuid

st.set_page_config(page_title="Chat App", layout="wide")

# ---------------------------
# SESSION STATE INITIALIZE
# ---------------------------

if "chats" not in st.session_state:
    st.session_state.chats = {}

if "current_chat_id" not in st.session_state:
    new_chat_id = str(uuid.uuid4())
    st.session_state.current_chat_id = new_chat_id
    st.session_state.chats[new_chat_id] = []

# ---------------------------
# SIDEBAR (Chat History)
# ---------------------------

st.sidebar.title("💬 Chats")

if st.sidebar.button("➕ New Chat"):
    new_chat_id = str(uuid.uuid4())
    st.session_state.current_chat_id = new_chat_id
    st.session_state.chats[new_chat_id] = []

for chat_id in st.session_state.chats.keys():
    if st.sidebar.button(f"Chat {chat_id[:6]}", key=chat_id):
        st.session_state.current_chat_id = chat_id

# ---------------------------
# MAIN CHAT WINDOW
# ---------------------------

st.title("🤖 Streamlit ChatGPT Clone")

current_chat = st.session_state.chats[st.session_state.current_chat_id]

# Display previous messages
for message in current_chat:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ---------------------------
# CHAT INPUT (Bottom)
# ---------------------------

prompt = st.chat_input("Type your message...")

if prompt:
    # Add user message
    current_chat.append({"role": "user", "content": prompt})

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Dummy bot response (replace with LLM later)
    response = f"You said: {prompt}"

    current_chat.append({"role": "assistant", "content": response})

    with st.chat_message("assistant"):
        st.markdown(response)