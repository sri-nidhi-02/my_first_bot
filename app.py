import streamlit as st
import time

# Set up the page
st.set_page_config(page_title="Streamlit Chatbot", page_icon="🤖")

# Title of the chatbot app
st.title("Chatbot with Continuous Stream")

# Initialize session state for message storage
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Chat Input
def get_user_input():
    input_text = st.text_input("You:", key="input")
    return input_text

# Bot response generator (simulate streaming with time delay)
def bot_response_streamed(user_input):
    response = "Processing your query..."  # Simulate processing
    with st.empty():  # Placeholder for the bot's response
        for i in range(3):  # Simulate bot "thinking"
            response += "."
            st.write(response)  # Update the placeholder
            time.sleep(1)
    return f"Response to '{user_input}'"

# Handle user input and bot response
user_input = get_user_input()
if user_input:
    # Store user message
    st.session_state.messages.append({"user": user_input})

    # Simulate bot thinking/processing with continuous streaming
    bot_reply = bot_response_streamed(user_input)

    # Store bot message
    st.session_state.messages.append({"bot": bot_reply})

# Display the conversation history
for message in st.session_state["messages"]:
    if "user" in message:
        st.chat_message("user").write(message["user"])
    if "bot" in message:
        st.chat_message("bot").write(message["bot"])
