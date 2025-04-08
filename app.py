import os
from groq import Groq


print("hello")
# Initialize Groq client
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))  # Use environment variable for security
print(client.api_key)

def get_chat_completion(prompt):
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama3-8b-8192",
        temperature=0.7,
    )

    print(chat_completion.choices[0].message.content)
    return chat_completion.choices[0].message.content


import streamlit as st

st.title("Bob The Builder")
st.subheader("What are we building today?")

user_input = st.text_input("You: ", "")

if user_input:
    if 'fix' in user_input.lower() or 'build' in user_input.lower():

        prompt = f"{user_input} (Please respond in a light and funny tone.)"

        bot_response = get_chat_completion(user_input)
        if bot_response:
            st.text(f"Bob: {bot_response}")

    else:
        st.write("I can only help with questions that involve fixing or building! Try again, Buddy")



