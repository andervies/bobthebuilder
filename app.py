import os
from groq import Groq


print("hello")
# Initialize Groq client
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))  # Use environment variable for security
print(client.api_key)

def get_chat_completion(prompt):
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama3-8b-8192"  # Ensure this model is available in your account
    )

    print(chat_completion.choices[0].message.content)
    return chat_completion.choices[0].message.content


import streamlit as st

st.title("Groq Chatbot")

user_input = st.text_input("You: ", "")

if user_input:
    bot_response = get_chat_completion(user_input)
    st.text(f"Bot: {bot_response}")



