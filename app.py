import streamlit as st
import openai

# Set up OpenAI API key (replace with your actual key)
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("Chat with AI")

# Create a text input for user queries
user_input = st.text_input("You: ")

if st.button("Send"):
    if user_input:
        # Call OpenAI API to get a response
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or "gpt-4" if you have access
            messages=[{"role": "user", "content": user_input}]
        )
        # Display the AI's response
        st.write(f"AI: {response['choices'][0]['message']['content']}")
    else:
        st.write("Please enter a message.")
